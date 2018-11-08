def total_score(word_scores):
    total_score = 0.0
    sum = 0.0
    for score in word_scores:
        total_score += score[0] / float(score[1])
        sum += 1.0 / float(score[1])
    total_score = total_score / sum
    return total_score

def calculate_sentiment(word):
    swn_path = "/Users/lorenzobraconi/Desktop/WordEmbedding/SentiWordNet_3.0.0_20130122.txt"
    score_sentiment = 0
    word_scores = []
    with open(swn_path,'r') as swn:
        content = swn.readlines()
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
        score_sentiment = total_score(word_scores)
        print score_sentiment

calculate_sentiment('herbal_medicine')
