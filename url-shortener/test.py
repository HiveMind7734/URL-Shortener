url = {}
import json
# url['phub'] = {'url':'www.pornhub.com'}
url['phub'] = {'file':'www.pornhub.com'}
url['pedu'] = {'url':'www.python.edu'}
url['logs1'] = {'file':'file1.txt'}
url['logs2'] = {'file':'file2.txt'}
url['logs3'] = {'file':'file3.txt'}
print(url['phub'])

if 'phub' in url.keys():
  print('its alive!')
else:
  print('nothing there')

pjson = {"users": [
  {"username" : "SammyShark", "location" : "Indian Ocean"},
  {"username" : "JesseOctopus", "location" : "Pacific Ocean"},
  {"username" : "DrewSquid", "location" : "Atlantic Ocean"},
  {"username" : "JamieMantisShrimp", "location" : "Pacific Ocean"}
] }

with open('urls.json','w') as url_file:  #only move forward if you can open this file.
    json.dump(url,url_file )



url['logs4'] = {'file':'file3.txt'}
with open('urls.json','w') as url_file:  #only move forward if you can open this file.
    json.dump(url,url_file )

