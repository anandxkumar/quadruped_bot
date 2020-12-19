# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:35:06 2020

@author: anand
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:19:33 2020

@author: anand
"""

import serial

ser1=serial.Serial('COM8',115200)
import speech_recognition as sr     # import the library
 
a=''
b=input("Enter y or n")
while b=='y' :
    r = sr.Recognizer()                 # initialize recognizer
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)        # listen to the source
        try:
            text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
            if text=='forward' :
                a='f'
            elif text=='backward':
                a='b'
            elif text=='sit':
                a='i'
            elif text=='stand':
                a='s'
            elif text=='left':
                a='l'
            elif text=='right':
                a='r'
            elif text=='hello':
                a='h'
        except:
            print("Sorry could not recognize your voice")
    ser1.write(a.encode())
    b=input("Enter Y or N")