import requests, time, speech
from BeautifulSoup import BeautifulSoup
from threading import Thread


def extractandsay(b):
    print "do you want me to read the news?"
    speech.say("do you want me to read the news?")
    ans = speech.input()
    sp = True if 's' in ans.lower() else False
    for item in b.findAll('item'):
        title = item.findAll('title')[0].text
        print title
        if sp:
            speech.say(title + '.')
        time.sleep(.5)


url = "http://indianexpress.com/section/india/feed/"
b = BeautifulSoup(requests.get(url).content)

Thread(target=extractandsay, args=(b,)).start()