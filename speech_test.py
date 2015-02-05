import speech

speech.say("hello")
while True:
    phrase = speech.input()
    print phrase
    if phrase.lower() == "exit":
        break
    speech.say("You said %s" % phrase)