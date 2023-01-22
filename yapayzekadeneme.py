import speech_recognition as sr

import pyttsx3

from gtts import gTTS

r = sr.Recognizer()
with sr.Microphone() as source:
        print("Sizi Dinliyorum...")
        audio = r.listen(source)
        metin = str(r.recognize_google(audio,language = "tr"))
        print("Söylediğiniz şey: "+metin)



