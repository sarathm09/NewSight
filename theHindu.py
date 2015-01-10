import requests, time, speech
from BeautifulSoup import BeautifulSoup
from threading import Thread


def extractandsay(b):
	for item in b.findAll('item'):
		title = item.findAll('title')[0].text
		print title
		speech.say(title)
		time.sleep(.5)


url = "http://www.thehindu.com/?service=rss"
b = BeautifulSoup(requests.get(url).content)

Thread(target=extractandsay, args=(b,)).start()