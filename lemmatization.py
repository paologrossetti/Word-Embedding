# -*- coding: utf-8 -*-
import nltk
import re

from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return 'o'

wiki_path = '/home/paolo/Scrivania/wiki.txt'
regex_frasi = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
regex_puntegg = '[.,\/#!$%\^&\*;:{}=\-_`~()"\'–]'

with open('/home/paolo/Scrivania/dataset_lemmatization.txt','a+') as output:
    with open(wiki_path,'r') as wiki:
        wnl = WordNetLemmatizer()
        text = wiki.read().decode('utf8')
        sentences = re.split(regex_frasi,text)
        for sentence in sentences:
            tokens = word_tokenize(sentence)  # Generate list of tokens
            tokens_pos = pos_tag(tokens)
            for token_pos in tokens_pos:
                token_clean = re.sub(regex_puntegg, "", token_pos[0])
                if token_clean!="":
                    pos_word = get_wordnet_pos(token_pos[1])
                    token_to_lower = token_pos[0].lower()
                    try:
                        if pos_word!='o':
                            lemma = wnl.lemmatize(token_to_lower, pos_word)
                        else:
                            lemma = wnl.lemmatize(token_to_lower)
                        #print (lemma+'#'+pos_word).encode('utf8')
                        output.write((lemma+'#'+pos_word).encode('utf8')+' ')
                    except UnicodeDecodeError:
                        print 'Errore in ',sentence

