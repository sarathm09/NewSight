import requests, time, speech
from BeautifulSoup import BeautifulSoup

def extractandsay():
    print "welcome to NewSight"
    speech.say("welcome to NewSight")

    print "If you want guidelines, say yes. Else say no to proceed to read news"
    speech.say("If you want guidelines, say yes. Else say not to proceed to read news")
    opt = speech.input()
    if 'yes' in opt.lower():
        speech.say("NewSight coz you deserve to know the things around you.")
        speech.say("NewSight application helps you become aware of the daily changing world. ")
        speech.say("You can listen.to all the important genres of news through NewSight. ")
        speech.say("We present to you leading Indian dailies like The Hindu, The Deccan Herald and The Indian Express.")
        speech.say("Here are some guidelines which will help you through NewSight")
        speech.say("Choose the newspaper from the available menu by saying the corresponding name out.")
        speech.say("Select the required category from the available menu and say yes to proceed.")
        speech.say("After the headline is read out, if you wish to go into details, say yes on prompt.")
        speech.say("You can always come back to the main menu by interrupting the system with a stop")
        extractandsay()
    elif 'no' in opt.lower():
        print "Choose newspaper : The Hindu  Deccan Herald  Indian Express"
        speech.say("Choose newspaper : The Hindu  Deccan Herald  Indian Express")
        pap = speech.input()
        if "the hindu" in pap.lower():
            def hindu():
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
                        def readnews(b11):
                            for item in b11.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    hindu()
                                time.sleep(.5)

                        readnews(b11)

                    elif 'business' in numb.lower():
                        def readbusiness(b12):
                            for item in b12.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    hindu()
                                time.sleep(.5)

                        readbusiness(b12)

                    elif 'sport' in numb.lower():
                        def readsports(b13):
                            for item in b13.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    hindu()
                                time.sleep(.5)

                        readsports(b13)

                    elif 'entertainment' in numb.lower():
                        def readentertainment(b14):
                            for item in b14.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    hindu()
                                time.sleep(.5)
                        readentertainment(b14)

            url11 = "http://www.thehindu.com/news/?service=rss"
            b11 = BeautifulSoup(requests.get(url11).content)

            url12 = "http://www.thehindu.com/business/?service=rss"
            b12 = BeautifulSoup(requests.get(url12).content)

            url13 = "http://www.thehindu.com/sport/?service=rss"
            b13 = BeautifulSoup(requests.get(url13).content)

            url14 = "http://www.thehindu.com/entertainment/?service=rss"
            b14 = BeautifulSoup(requests.get(url14).content)

            hindu()

        elif "deccan" in pap.lower():
            def deccan():
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
                        def readnews(b21):
                            for item in b21.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    deccan()
                                time.sleep(.5)

                        readnews(b21)

                    elif 'business' in numb.lower():
                        def readbusiness(b22):
                            for item in b22.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    deccan()
                                time.sleep(.5)

                        readbusiness(b22)

                    elif 'sport' in numb.lower():
                        def readsports(b23):
                            for item in b23.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    deccan()
                                time.sleep(.5)

                        readsports(b23)

                    elif 'entertainment' in numb.lower():
                        def readentertainment(b24):
                            for item in b24.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    deccan()
                                time.sleep(.5)

                        readentertainment(b24)


            url21 = "http://www.deccanherald.com/rss/news.rss"
            b21 = BeautifulSoup(requests.get(url21).content)

            url22 = "http://www.deccanherald.com/rss/business.rss"
            b22 = BeautifulSoup(requests.get(url22).content)

            url23 = "http://www.deccanherald.com/rss/sports.rss"
            b23 = BeautifulSoup(requests.get(url23).content)

            url24 = "http://www.deccanherald.com/rss/entertainment.rss"
            b24 = BeautifulSoup(requests.get(url24).content)

            deccan()

        elif "indian express" in pap.lower():
            def indian():
                print "welcome to The Indian Express"
                speech.say("welcome to The Indian Express")
                print "Choose genre :  News  Politics  Sports  Entertainment"
                speech.say("Choose genre :  News  Politics  Sports  Entertainment")
                numb = speech.input()
                print "say yes if you want me to read the news. else no."
                speech.say('say yes if you want me to read the news. else no.')
                answ = speech.input()
                sps = True if 's' in answ.lower() else False
                if sps:
                    if 'news' in numb.lower():
                        def readnews(b31):
                            for item in b31.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    indian()
                                time.sleep(.5)

                        readnews(b31)

                    elif 'politics' in numb.lower():
                        def readpolitics(b32):
                            for item in b32.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    indian()
                                time.sleep(.5)

                        readpolitics(b32)

                    elif 'sport' in numb.lower():
                        def readsports(b33):
                            for item in b33.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    indian()
                                time.sleep(.5)

                        readsports(b33)

                    elif 'entertainment' in numb.lower():
                        def readentertainment(b34):
                            for item in b34.findAll('item'):
                                title = item.findAll('title')[0].text
                                print title
                                speech.say(title + '.')
                                print "For details say yes. For menu say back. else no"
                                speech.say("For details say yes. For menu say back. else no")
                                ans = speech.input()
                                sp = True if 's' in ans.lower() else False
                                if sp:
                                    description = item.findAll('description')[0].text
                                    print description
                                    speech.say(description + '.')
                                elif 'back' in ans.lower():
                                    indian()
                                time.sleep(.5)

                        readentertainment(b34)


            url31 = "http://indianexpress.com/section/india/feed/"
            b31 = BeautifulSoup(requests.get(url31).content)

            url32 = "http://indianexpress.com/section/india/politics/feed/"
            b32 = BeautifulSoup(requests.get(url32).content)

            url33 = "http://indianexpress.com/section/sports/feed/"
            b33 = BeautifulSoup(requests.get(url33).content)

            url34 = "http://indianexpress.com/section/entertainment/feed/"
            b34 = BeautifulSoup(requests.get(url34).content)

            indian()

if __name__ == '__main__':
    extractandsay()