import requests, json, os, urllib.request

with urllib.request.urlopen("http://labs.bible.org/api/?passage=votd&type=json") as url:
    data = json.loads(url.read().decode())
print(data)
    
book = data[0]["bookname"]
chapter = data[0]["chapter"]
verse = data[0]["verse"]
text = data[0]["text"]


post = book + " " + chapter + ":" + verse + " " + '\n' + text
output = { 'bot_id' : os.getenv('GROUPME_BOT_ID'),
         'text': post }
requests.post('https://api.groupme.com/v3/bots/post',
              params = output)
