import requests, json, os, urllib.request, string

with urllib.request.urlopen("http://labs.bible.org/api/?passage=votd&type=json") as url:
    data = json.loads(url.read().decode())
print(data)
with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?id=4553433&APPID=a14242230083e21bb57fc9a3aceaf147") as url:
    weather = json.loads(url.read().decode())

description = weather["weather"][0]['description']
descriptionCaps = description.title()
lowTempK = weather["main"]["temp_min"]
highTempK = weather["main"]["temp_max"]

lowTempF = str(int(9 / 5 * lowTempK - 459.67))
highTempF = str(int(9 / 5 * highTempK - 459.67))

weatherOutput = "The weather in Tulsa, OK is: " + '\n' + '\t' + descriptionCaps + ", with a High of " + highTempF + "°F and a Low of " + lowTempF + "°F"
print(weatherOutput)
book = data[0]["bookname"]
chapter = data[0]["chapter"]
verse = data[0]["verse"]
text = data[0]["text"]

if len(data) > 1:
    text = "%s %s" % (verse, text)
    verse += '-' + data[len(data)-1]["verse"]
    for i in range(1, len(data)):
        text += " %s %s" % (data[i]["verse"], data[i]["text"])

post = " %s %s:%s ~ \n \t %s \n %s " % (book, chapter, verse, text, weatherOutput)
output = { 'bot_id' : os.getenv('GROUPME_BOT_ID'),
         'text': post }
requests.post('https://api.groupme.com/v3/bots/post',
              params = output)
