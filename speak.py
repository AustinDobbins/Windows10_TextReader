import os 
import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def speak(text):
	language="en"
	tts = gTTS(text=text)
	filename = "voice.mp3"
	tts.save(filename)
	playsound('voice.mp3')

speak("Hi, change the text on line fourteen to make me say something new") 