import csv

#funzione che calcola la media degli score di una parola
def total_score(word_scores):
    total_score = 0.0
    for score in word_scores:
        total_score += score[0]
    average_score = total_score / len(word_scores)
    return average_score

#funzione che calcola lo score se una parola e' presente in SentiWordNet, altrimenti torna 'Not found'
def calculate_sentiment(word_pos, content):
    word_scores = []
    for row in content:
        if not row.strip().startswith('#'):
            list_of_row = row.split('\t')
            if not len(list_of_row)==6:
                raise Exception('Tabulazione errata nel file')
            pos_row = list_of_row[0]
            word = word_pos[:-2]
            pos = word_pos[-1:]
            if pos == pos_row: #per ottimizzare la ricerca consideriamo solo le righe con POS della parola che stiamo cercando
                synTermsSplit = list_of_row[4].split(' ')
                for synTermSplit in synTermsSplit:
                    synTermAndRank = synTermSplit.split('#')
                    if word == synTermAndRank[0]: #se la parola che stiamo cercando e' stata trovata
                       word_score = float(list_of_row[2]) - float(list_of_row[3]) #calcoliamo lo score: positivo - negativo
                       word_scores.append([word_score,synTermAndRank[1]]) #salviamo in una lista il valore dello score per quell'occorrenza
    if word_scores: #se la lista non e' vuota
        score_sentiment = total_score(word_scores) #calcoliamo lo score medio
        return score_sentiment
    else:
        return 'Not found' #altrimenti torniamo 'Not found'

#funzione che associa una classe di sentiment ad una parola in base al suo score medio - 0.15 e' la soglia di sentiment adottata
def classified_sentiment(sentiment):
    if -1 <= sentiment < -0.15:
        return 'Negativo'
    elif sentiment <= 0.15:
        return 'Neutro'
    else:
        return 'Positivo'

#path del dizionario SentiWordNet che abbiamo utilizzato per calcolare il sentiment
swn_path = '/home/paolo/Scaricati/home/swn/www/admin/dump/SentiWordNet_3.0.0_20130122.txt'
with open(swn_path, 'r') as swn, open('/home/paolo/Scrivania/word-embedding.csv','r') as word_embedding: #il 2ndo e' il path del file prodotto da word_embedding.py
    content = swn.readlines()
    reader = csv.reader(word_embedding)
    with open('/home/paolo/Scrivania/we_in_swnet.csv','w') as we_in_swnet: #output prodotto
        writer_wis = csv.writer(we_in_swnet, lineterminator='\n')
        for row in reader: #per ogni riga del file del Word Embedding
            sentiment = calculate_sentiment(row[0], content) #ne calcoliamo il sentiment
            if sentiment != 'Not found': #se la parola e' presente in SentiWordNet
                senti_class = classified_sentiment(sentiment) #in base allo score associamo una classe
                writer_wis.writerow([senti_class] + row) #scriviamo tutta la riga in cui il primo elemento e' il suo sentiment





