import json
import os

import re

i=0
path_json_directory = '/Users/lorenzobraconi/Desktop/json'
with open('/Users/lorenzobraconi/Desktop/wiki.txt','a+') as output:
    for path, subdirs, files in os.walk(path_json_directory):
        for name in files:
            i=i+1
            print i
            with open(os.path.join(path, name)) as f:
                s = f.read().split('\n')
                for article in s:
                    try:
                        data=json.loads(article)
                        text_with_title = data['text']
                        text_with_newline = text_with_title.split("\n\n",1)[1]
                        text = text_with_newline.replace('\n',' ')
                        regex = r"( [A-Z][a-z]?)\."
                        text_clean = re.sub(regex,"",text)
                        output.write(text_clean.encode('utf8'))
                    except IndexError:
                        print (os.path.join(path, name),data['title'],'No testo per questo titolo')
                    except ValueError:
                        print (os.path.join(path, name),data['title'],'Fine file')
            f.close()
output.close()