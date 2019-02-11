# -*- coding: utf-8 -*-
import nltk
import re

from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#le 2 istruzioni seguenti devono essere eseguite la prima volta, poi possono essere commentate
nltk.download('punkt') #file della liberia nltk che vengono scaricati per il POS tagging e la lemmatization
nltk.download('averaged_perceptron_tagger') #file della liberia nltk che vengono scaricati per il POS tagging e la lemmatization

def get_wordnet_pos(treebank_tag): #funzione che permette di ricodurre il POS calcolato al POS di SentiWordNet

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return 'o' #se il POS della parola non è uno dei precedenti gli assegnamo un valore di default(o=other)

wiki_path = '/home/paolo/Scrivania/wiki.txt' #path del testo prodotto da wiki_text.py
regex_frasi = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s' #regola regex per rilevare le frasi
regex_puntegg = '[.,\/#!$%\^&\*;:{}=\-_`~()"\'–]' #regola regex per individuare caratteri di punteggiatura

with open('/home/paolo/Scrivania/dataset_lemmatization.txt','a+') as output: #il file di output e' aperto in modalita' APPEND
    with open(wiki_path,'r') as wiki:
        wnl = WordNetLemmatizer()
        text = wiki.read().decode('utf8')
        sentences = re.split(regex_frasi,text) #splittiamo il testo in frasi
        for sentence in sentences: #per ogni frase
            tokens = word_tokenize(sentence) #produce una lista di parole
            tokens_pos = pos_tag(tokens) #produce una lista di liste in cui ogni lista contiene la parola ed il POS associato
            for token_pos in tokens_pos:
                token_clean = re.sub(regex_puntegg, "", token_pos[0]) #se la parola è un carattere di punteggiatura viene sostituita con ""
                if token_clean!="": #se la parola non è un carattere di punteggiatura
                    pos_word = get_wordnet_pos(token_pos[1]) #riconduciamo il pos al POS tagging di SentiWordNet
                    token_to_lower = token_pos[0].lower()
                    try:
                        if pos_word!='o': #se la parola ha un POS diverso da others
                            lemma = wnl.lemmatize(token_to_lower, pos_word) #lemmatizziamo la parola sulla base del POS
                        else:
                            lemma = wnl.lemmatize(token_to_lower) #altrimenti lemmatizziamo la parola considerando il POS di default del metodo
                        output.write((lemma+'#'+pos_word).encode('utf8')+' ') #scriviamo parola#POS nel file
                    except UnicodeDecodeError:
                        print 'Errore in ',sentence

