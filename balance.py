import csv
import random

with open('/home/paolo/Scrivania/015/we_in_swnet.csv', 'r') as data:
    reader = csv.reader(data)
    neutri, positivi, negativi = [], [], []
    for row in reader:
        if row[0]=='Neutro':
            neutri.append(row)
        elif row[0] == 'Positivo':
            positivi.append(row)
        else:
            negativi.append(row)
    n_neutri = len(neutri)
    n_positivi = len(positivi)
    n_negativi = len(negativi)
    minimo = n_neutri
    if n_positivi < minimo:
        minimo = n_positivi
    if n_negativi < minimo:
        minimo = n_negativi
    random_neutri = random.sample(neutri, minimo)
    random_positivi = random.sample(positivi, minimo)
    random_negativi = random.sample(negativi, minimo)
    with open('/home/paolo/Scrivania/015/we_in_swnet_balanced.csv', 'w') as balanced:
        writer_ws = csv.writer(balanced, lineterminator='\n')
        writer_ws.writerows(random_neutri)
        writer_ws.writerows(random_positivi)
        writer_ws.writerows(random_negativi)
