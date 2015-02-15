import requests, time, speech
from BeautifulSoup import BeautifulSoup
from threading import Thread


def extractandsay():
    print "welcome to Deccan herald"
    speech.say("welcome to Deccan Herald")
    print "Choose genre  : News Business Sports Entertainment"
    speech.say("Choose genre  : News Business Sports Entertainment")
    numb = speech.input()
    print "Say yes if you want me to read the news. Else no"
    speech.say("Say yes if you want me to read the news. Else no")
    answ = speech.input()
    sps = True if 's' in answ.lower() else False
    if sps:
        if 'news' in numb.lower():
            def readnews(b1):
                for item in b1.findAll('item'):
                    title = item.findAll('title')[0].text
                    print title
                    speech.say(title + '.')
                    print "Say yes if you want me to read it in detail? Else no"
                    speech.say("Say yes if you want me to read it in detail? Else no")
                    ans = speech.input()
                    sp = True if 's' in ans.lower() else False
                    if sp:
                        description = item.findAll('description')[0].text
                        print description
                        speech.say(description + '.')
                    time.sleep(.5)

            Thread(target=readnews, args=(b1,)).start()

        elif 'business' in numb.lower():
            def readbusiness(b2):
                for item in b2.findAll('item'):
                    title = item.findAll('title')[0].text
                    print title
                    speech.say(title + '.')
                    print "Say yes if you want me to read it in detail? Else no"
                    speech.say("Say yes if you want me to read it in detail? Else no")
                    ans = speech.input()
                    sp = True if 's' in ans.lower() else False
                    if sp:
                        description = item.findAll('description')[0].text
                        print description
                        speech.say(description + '.')
                    time.sleep(.5)

            Thread(target=readbusiness, args=(b2,)).start()

        elif 'sport' in numb.lower():
            def readsports(b3):
                for item in b3.findAll('item'):
                    title = item.findAll('title')[0].text
                    print title
                    speech.say(title + '.')
                    print "Say yes if you want me to read it in detail? Else no"
                    speech.say("Say yes if you want me to read it in detail? Else no")
                    ans = speech.input()
                    sp = True if 's' in ans.lower() else False
                    if sp:
                        description = item.findAll('description')[0].text
                        print description
                        speech.say(description + '.')
                    time.sleep(.5)

            Thread(target=readsports, args=(b3,)).start()

        elif 'entertainment' in numb.lower():
            def readentertainment(b4):
                for item in b4.findAll('item'):
                    title = item.findAll('title')[0].text
                    print title
                    speech.say(title + '.')
                    print "Say yes if you want me to read it in detail? Else no"
                    speech.say("Say yes if you want me to read it in detail? Else no")
                    ans = speech.input()
                    sp = True if 's' in ans.lower() else False
                    if sp:
                        description = item.findAll('description')[0].text
                        print description
                        speech.say(description + '.')
                    time.sleep(.5)

            Thread(target=readentertainment, args=(b4,)).start()


url1 = "http://www.deccanherald.com/rss/news.rss"
b1 = BeautifulSoup(requests.get(url1).content)

url2 = "http://www.deccanherald.com/rss/business.rss"
b2 = BeautifulSoup(requests.get(url2).content)

url3 = "http://www.deccanherald.com/rss/sports.rss"
b3 = BeautifulSoup(requests.get(url3).content)

url4 = "http://www.deccanherald.com/rss/entertainment.rss"
b4 = BeautifulSoup(requests.get(url4).content)
if __name__ == '__main__':
    extractandsay()