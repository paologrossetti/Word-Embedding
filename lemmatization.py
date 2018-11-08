#import nltk

#nltk.download('wordnet')

#from nltk.stem.wordnet import WordNetLemmatizer

#lemmatizer = WordNetLemmatizer()

#print(lemmatizer.lemmatize(""))

import nltk
#nltk.download('punkt')

#nltk.download('averaged_perceptron_tagger')



from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
s = "some betters are crazy"
tokens = word_tokenize(s)  # Generate list of tokens
tokens_pos = pos_tag(tokens)


from nltk.corpus import wordnet

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

print(get_wordnet_pos('NNS'))




print(wnl.lemmatize("better",get_wordnet_pos('JJ')))



print(tokens_pos)

#['Resumption', 'of', 'the', 'session', 'I', 'declare', u'resume', 'the', 'session', 'of', 'the', 'European', 'Parliament', u'adjourn', 'on', 'Friday', '17', 'December', '1999', ',', 'and', 'I', 'would', 'like', 'once', 'again', 'to', 'wish', 'you', 'a', 'happy', 'new', 'year', 'in', 'the', 'hope', 'that', 'you', u'enjoy', 'a', 'pleasant', 'festive', 'period', '.']