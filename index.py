import speech_recognition as sr
import re
import pyttsx3

nome = " "
while(True):

    microfone = sr.Recognizer()
    with sr.Microphone() as source:
       engine = pyttsx3.init()
       engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")
       microfone.adjust_for_ambient_noise(source)

       print("Vamos começar, fale alguma coisa")

       audio = microfone.listen(source)

       try:
           frase = microfone.recognize_google(audio, language = "pt-BR")

           if(re.search(r'\b'+"ajudar"+r'\b',format(frase))):
               engine.say("Ajuda")
               engine.runAndWait()
               print("Algo relacionado a ajuda.")

           elif (re.search(r'\b'+"meu nome é"+r'\b',format(frase))):
               temporario = re.search('meu nome é (.*)', format(frase))
               nome = temporario.group(1)
               print("Seu nome é "+nome)
               engine.say("Nome falado foi" + nome)
               engine.runAndWait()

           print("Você falou: "+frase)
       except sr.UnknownValueError:
           print("ops, algo deu errado")

