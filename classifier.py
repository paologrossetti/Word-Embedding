import random
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

with open('/home/paolo/Scrivania/015/we_in_swnet.csv', 'r') as dataset: #path del file prodotto da calculate_sentiment.py
    rows = [row.split(',') for row in dataset] #produciamo una lista di liste in cui ogni lista e' una riga del dataset che contiene sentiment,parola e tutte le 128 features
    testset_size = int(len(rows)*0.2) #calcoliamo il 20% del numero di righe totali (Hold-out 80/20)
    random_rows = random.sample(rows, testset_size) #prendiamo le righe che saranno usate per il testing
    random_words, features_test, labels_test = [],[], []
    for random_row in random_rows: #costruiamo il dataset per il testing
        random_words.append(random_row[1])
        features_test.append(random_row[2:])
        labels_test.append(random_row[0])
    features_train,labels_train = [],[]
    for line in rows: #costruiamo il dataset per il training
        if line[1] not in random_words:
            features_train.append(line[2:])
            labels_train.append(line[0])

for k in range(1,9,1): #loop sul k del k-NN da 1 a 9
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(features_train,labels_train) #addestriamo il modello
    predicted = model.predict(features_test) #fa la predizione sul testing
    from sklearn.metrics import classification_report, confusion_matrix
    miss=0
    for i in range(0,testset_size,1): #calcola il numero di misclassificati
        if labels_test[i] != predicted[i]:
            miss = miss+1
    errore = float(miss)/testset_size #calcoliamo il classification error
    accuracy = 1 - errore #calcoliamo l'accuracy
    print 'accuracy per k=',k,' ',accuracy
    print(pd.DataFrame(confusion_matrix(labels_test,predicted,labels=['Negativo','Neutro','Positivo']),index=['true:Negativo','true:Neutro','true:Positivo'],columns=['pred:Negativo','pred:Neutro','pred:Positivo']))
    print(confusion_matrix(labels_test, predicted,labels=['Negativo','Neutro','Positivo']))
    print(classification_report(labels_test, predicted))
