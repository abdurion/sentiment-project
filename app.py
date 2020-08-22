import speech_recognition as sr
from textblob import TextBlob

r = sr.Recognizer()

PATH = 'sample.wav'

with sr.AudioFile(PATH) as source:
    audio = r.record(source)

mySentence = r.recognize_google(audio)
print(mySentence)

mySentence.sentiment
