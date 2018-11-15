import csv

def total_score(word_scores):
    total_score = 0.0
    for score in word_scores:
        total_score += score[0]
    average_score = total_score / len(word_scores)
    return average_score

def calculate_sentiment(word, content):
    score_sentiment = 0
    word_scores = []
    for row in content:
        if not row.strip().startswith('#'):
            list_of_row = row.split('\t')
            wordTypeMarker = list_of_row[0]
            if not len(list_of_row)==6:
                raise Exception('Tabulazione errata nel file')
            synTermsSplit = list_of_row[4].split(' ')
            for synTermSplit in synTermsSplit:
                synTermAndRank = synTermSplit.split('#')
                if word == synTermAndRank[0]:
                   word_score = float(list_of_row[2]) - float(list_of_row[3])
                   word_scores.append([word_score,synTermAndRank[1]])
    if word_scores:
        score_sentiment = total_score(word_scores)
        return score_sentiment
    else:
        return 'Not found'

def classified_sentiment(sentiment):
    if -1 <= sentiment < -0.15:
        return 'Negativo'
    elif sentiment <= 0.15:
        return 'Neutro'
    else:
        return 'Positivo'

swn_path = '/Users/lorenzobraconi/Desktop/SentiWordNet_3.0.0_20130122.txt'
with open(swn_path, 'r') as swn, open('/Users/lorenzobraconi/Desktop/output2.csv','r') as word_embedding:
    content = swn.readlines()
    reader = csv.reader(word_embedding)
    with open('/Users/lorenzobraconi/Desktop/word_sentiment.csv', 'w') as senti_we, open('/Users/lorenzobraconi/Desktop/we_in_swnet.csv','w') as we_in_swnet:
        writer_ws = csv.writer(senti_we, lineterminator='\n')
        writer_wis = csv.writer(we_in_swnet, lineterminator='\n')
        i=0
        for row in reader:
            i += 1
            print i
            sentiment = calculate_sentiment(row[0], content)
            if sentiment != 'Not found':
                senti_class = classified_sentiment(sentiment)
                writer_ws.writerow([row[0], senti_class, sentiment])
                writer_wis.writerow([senti_class] + row)







