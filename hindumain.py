import requests, time, speech
from BeautifulSoup import BeautifulSoup
from threading import Thread


def extractandsay():
    print "welcome to The Hindu"
    speech.say("welcome to The Hindu")
    print "Choose genre :  News  Business  Sports  Entertainment "
    speech.say("Choose genre :  News  Business  Sports  Entertainment ")
    numb = speech.input()
    print "say yes if you want me to read the news. else no."
    speech.say('say yes if you want me to read the news. else no.')
    answ = speech.input()
    sps = True if 's' in answ.lower() else False
    if sps:
        if 'news' in numb.lower():
            def readnews(b1):
                for item in b1.findAll('item'):
                    title = item.findAll('title')[0].text
                    print title
                    speech.say(title + '.')
                    print "say yes if you want me to read it in detail. else no."
                    speech.say("say yes if you want me to read it in detail. else no.")
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
                    print "say yes if you want me to read it in detail. else no"
                    speech.say("say yes if you want me to read it in detail. else no")
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
                    print "say yes if you want me to read it in detail. else no"
                    speech.say("say yes if you want me to read it in detail. else no")
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
                    print "say yes if you want me to read it in detail. else no"
                    speech.say("say yes if you want me to read it in detail. else no")
                    ans = speech.input()
                    sp = True if 's' in ans.lower() else False
                    if sp:
                        description = item.findAll('description')[0].text
                        print description
                        speech.say(description + '.')
                    time.sleep(.5)

            Thread(target=readentertainment, args=(b4,)).start()


url1 = "http://www.thehindu.com/news/?service=rss"
b1 = BeautifulSoup(requests.get(url1).content)

url2 = "http://www.thehindu.com/business/?service=rss"
b2 = BeautifulSoup(requests.get(url2).content)

url3 = "http://www.thehindu.com/sport/?service=rss"
b3 = BeautifulSoup(requests.get(url3).content)

url4 = "http://www.thehindu.com/entertainment/?service=rss"
b4 = BeautifulSoup(requests.get(url4).content)

if __name__ == '__main__':
    extractandsay()