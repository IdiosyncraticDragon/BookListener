# coding:utf-8
import pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
#for voice in voices:
#   engine.setProperty('voice', voice.id)  # changes the voice
#   print voice.id
#   engine.say(u'您好！')
engine.setProperty('voice', voices[-2].id)  # changes the voice
engine.say(u'您好！')
engine.runAndWait()
