# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:19:33 2020

@author: anand
"""

import serial

ser1=serial.Serial('COM8',115200)
import speech_recognition as sr     # import the library
b=0 
a=""
r = sr.Recognizer()                 # initialize recognizer
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    audio = r.listen(source)        # listen to the source
    try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
        if text=="forward":
            a='u'
            ser1.write(b'u')    
        elif text=="easy":
            a='l'
            ser1.write(b'l')
    except:
        print("Sorry could not recognize your voice")
        

    
