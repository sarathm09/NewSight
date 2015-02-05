import urllib2
from BeautifulSoup import BeautifulSoup
import re
import speech
import time


def main():
    while True:
        speech.say("What should I search for?")
        search = speech.input("What should I search for?")
        speech.say("Did you mean " + search + "?")
        print "Did you mean " + search + " ?"
        ans = speech.input()
        if ans.lower() == "yes":
            break
        time.sleep(1)

    print "Searching for " + search
    url = 'http://en.wikipedia.org/w/index.php?search=' + search.replace(' ', '+') + '&title=Special%3ASearch&go=Go'
    brks = '\[\d*\]'
    br = re.compile(brks)
    b = BeautifulSoup(urllib2.urlopen(url).read())
    p = b.("p")
    if "may refer to" in str(p[0]) or "no results" in str(p[0]):
        print "Oops, exact match not found, please try again.. "
        exit(0)
    else:
        data = ""
        for item in p:
            data += re.sub(br, '', item.text).replace("\n", "") + "\n"
            if len(data) > 1500:
                break
        print data
        speech.say(data)


if __name__ == "__main__":
    main()