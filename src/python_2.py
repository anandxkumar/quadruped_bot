# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:11:31 2020

@author: anand
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:19:33 2020

@author: anand
"""

import serial

ser1=serial.Serial('COM8',115200)
ser2=serial.Serial('COM7',115200)
import speech_recognition as sr     # import the library
r = sr.Recognizer()                 # initialize recognizer
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    audio = r.listen(source)        # listen to the source
    try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
        if "stand" in text.split(' '):
            ser1.write(b'm')    
        elif "down" in text.split(' '):
            ser1.write(b'n')
        elif "fire" in text.split(' '):
            ser2.write(b'x')
            ser1.write(b'x')
        elif "forward" in text.split(' '):
            ser1.write(b'o')
        elif "backward" in text.split(' '):
            ser1.write(b'p')
        elif "left" in text.split(' '):
            ser1.write(b'q')
        elif "right" in text.split(' '):
            ser1.write(b'r')
        elif "hi" in text.split(' '):
            ser1.write(b's')
    except:
        print("Sorry could not recognize your voice")
        

    
