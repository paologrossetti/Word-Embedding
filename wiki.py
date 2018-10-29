import sys
from gensim.corpora import WikiCorpus

def make_corpus(in_f, out_f):

	"""Convert Wikipedia xml dump file to text corpus"""

	output = open(out_f, 'w')
	wiki = WikiCorpus(in_f)

	i = 0
	for text in wiki.get_texts():
		output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
		i = i + 1
	output.close()
	print('Processing complete!')

make_corpus("/home/paolo/Scaricati/simplewiki-20170820-pages-meta-current.xml.bz2", "/home/paolo/Scrivania/wiki.txt")