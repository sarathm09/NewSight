import requests, time, speech
from BeautifulSoup import BeautifulSoup
from threading import Thread



def extractandsay():
    print "welcome to Hindu Newspaper"
    speech.say("welcome to Hindu Newspaper")
    print "do you want me to read the news?"
    speech.say("do you want me to read the news?")
    ans = speech.input()
    sp = True if 's' in ans.lower() else False
    print "Categories 1 News 2 Business 3 Sports 4 Entertainment"
    speech.say("Categories 1 News 2 Business 3 Sports 4 Entertainment")
    numb = speech.input()
    if sp:
            if 'news' in numb.lower():
                news()


            elif 'business' in numb.lower():
                business()

            elif 'sport' in numb.lower():
                sports()


            elif 'entertainment' in numb.lower():
                entertainment()

def news(b1):
    for item in b1.findAll('item'):
            title = item.findAll('title')[0].text
            print title
            speech.say(title + '.')
            time.sleep(.5)
    url1 = "http://www.thehindu.com/news/?service=rss"
    b1 = BeautifulSoup(requests.get(url1).content)
    Thread(target=news, args=(b1,)).start()

def business(b2):
    for item in b2.findAll('item'):
            title = item.findAll('title')[0].text
            print title
            speech.say(title + '.')
            time.sleep(.5)
    url2 = "http://www.thehindu.com/business/?service=rss"
    b2 = BeautifulSoup(requests.get(url2).content)
    Thread(target=business, args=(b2,)).start()

def sports(b3):
    for item in b3.findAll('item'):
                title = item.findAll('title')[0].text
                print title
                speech.say(title + '.')
                time.sleep(.5)
    url3 = "http://www.thehindu.com/sport/?service=rss"
    b3 = BeautifulSoup(requests.get(url3).content)
    Thread(target=sports, args=(b3,)).start()

def entertainment(b4):
    for item in b4.findAll('item'):
                title = item.findAll('title')[0].text
                print title
                speech.say(title + '.')
                time.sleep(.5)
    url4 = "http://www.thehindu.com/entertainment/?service=rss"
    b4 = BeautifulSoup(requests.get(url4).content)
    Thread(target=entertainment, args=(b4,)).start()

if __name__ == '__main__':
    extractandsay()



