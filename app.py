import requests, json, os, urllib.request

with urllib.request.urlopen("http://labs.bible.org/api/?passage=random&type=json") as url:
    data = json.loads(url.read().decode())
print(data)
    
book = data[0]["bookname"]
chapter = data[0]["chapter"]
verse = data[0]["verse"]
text = data[0]["text"]

if len(data) > 1:
    text = "%s %s" % (verse, text)
    verse += '-' + data[len(data)-1]["verse"]
    for i in range(1, len(data)):
        text += " %s %s" % (data[i]["verse"], data[i]["text"])

post = "%s %s:%s ~ \n \t %s" % (book, chapter, verse, text)
output = { 'bot_id' : os.getenv('GROUPME_BOT_ID'),
         'text': post }
requests.post('https://api.groupme.com/v3/bots/post',
              params = output)
