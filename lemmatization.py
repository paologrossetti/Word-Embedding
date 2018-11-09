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
        return ''

wiki_path = '/home/paolo/Scrivania/wiki.txt'
regex = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'

with open('/home/paolo/Scrivania/dataset_lemmatization.txt','a+') as output:
    with open(wiki_path,'r') as wiki:
        wnl = WordNetLemmatizer()
        text = wiki.read()
        sentences = re.split(regex,text)
        for sentence in sentences:
            tokens = word_tokenize(sentence)  # Generate list of tokens
            tokens_pos = pos_tag(tokens)
            for token_pos in tokens_pos:
                pos_word = get_wordnet_pos(token_pos[1])
                if pos_word!='':
                    lemma = wnl.lemmatize(token_pos[0].encode('utf8'), pos_word)
                else:
                    lemma = wnl.lemmatize(token_pos[0].encode('utf8'))
                output.write(lemma.encode('utf8'))







print(wnl.lemmatize("TyszkiewiczównaKalenicka",get_wordnet_pos('NN')))

