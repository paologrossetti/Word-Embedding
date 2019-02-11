import json
import os
import re

path_json_directory = '/home/paolo/Scrivania/json' #questo path si riferisce alla cartella che contiene gli articoli in formato JSON, prodotta dallo script WikiExtractor-attardi.py
with open('/home/paolo/Scrivania/wiki.txt','a+') as output: #il file di output e' aperto in modalita APPEND
    for path, subdirs, files in os.walk(path_json_directory):
        for name in files:
            with open(os.path.join(path, name)) as f:
                s = f.read().split('\n')
                for article in s:
                    try:
                        data=json.loads(article)
                        text_with_title = data['text'] #estrae il valore del campo text che contiene il titolo dell'articolo ed il testo
                        text_with_newline = text_with_title.split("\n\n",1)[1] #prendiamo solo il testo dell'articolo
                        text = text_with_newline.replace('\n',' ')
                        regex = r"( [A-Z][a-z]?)\." #regola regex che ci consente di rilevare acronimi
                        text_clean = re.sub(regex,"",text) #sostituiamo gli acronimi con ""(vuoto)
                        output.write(text_clean.encode('utf8')) #scriviamo il testo nel file
                    except IndexError:
                        print (os.path.join(path, name),data['title'],'No testo per questo titolo')
                    except ValueError:
                        print (os.path.join(path, name),data['title'],'Fine file')
            f.close()
output.close()