import random
from sklearn.neighbors import KNeighborsClassifier


with open('/home/paolo/Scrivania/we_in_swnet.csv', 'r') as dataset:
    rows = [row.split(',') for row in dataset]
    random_rows = random.sample(rows, 50)
    random_words, features_test, labels_test = [],[], []
    for random_row in random_rows:
        random_words.append(random_row[1])
        features_test.append(random_row[2:])
        labels_test.append(random_row[0])
    features_train,labels_train = [],[]
    for line in rows:
        if line[1] not in random_words:
            features_train.append(line[2:])
            labels_train.append(line[0])

for k in range(1,20,2):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(features_train,labels_train)
    predicted = model.predict(features_test)
    from sklearn.metrics import classification_report, confusion_matrix
    miss=0
    for i in range(0,50,1):
        if labels_test[i] != predicted[i]:
            miss = miss+1
        #print random_words[i], labels_test[i], predicted[i]
    errore = float(miss)/50
    accuracy = 1 - errore
    #print 'erroreeeee per k=',k,' ',errore
    print 'accuracy per k=',k,' ',accuracy
    print(confusion_matrix(labels_test, predicted))
    #print(classification_report(labels_test, predicted))
