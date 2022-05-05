from ctypes.wintypes import MSG
from numpy import take
from pyautogui import click
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess as sp
from time import sleep


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good night!")

    speak("Hello! Susan here!.  How can i help you veda!")

    
        
def OnlineClass(Subject):
    
    if "English" in Subject:
        from OnlineClasses.Links import English
        Link = English()
        
        webbrowser.open(Link)
        speak("please wait sir while i connect you to Google meet!")
        sleep(20)
        click(x=707, y=765)
        sleep(3)
        click(x=611, y=766)
        sleep(2)
        click(x=1122, y=664)
        sleep(1)
        click(x=1349, y=534)
        speak("Waiting for venkataramana sir to admit you sir !")
        
    elif "environment" in Subject:
        from OnlineClasses.Links import Environment
        Link = Environment()
        
        webbrowser.open(Link)
        speak("please wait sir connecting you to Google meet!")
        sleep(20)
        click(x=707, y=765)
        sleep(3)
        click(x=611, y=766)
        sleep(2)
        click(x=1122, y=664)
        sleep(1)
        click(x=1349, y=534)
        speak("Waiting for Maha bala sir to admit you sir !")
        
    
    elif "analytical technique" in Subject:
        from OnlineClasses.Links import ATM
        Link = ATM()
        
        webbrowser.open(Link)
        speak("Please wait sir. Connecting you to Teams!")
        sleep(20)
        click(x=1225, y=512)
        sleep(39)
        click(x=772, y=684)
        sleep(2)
        click (x=1011, y=681)
        sleep(2)
        click (x=1102, y=618)
        speak("Joining the Chandru sir's class!")
    
    elif "organizational" in Subject:
        from OnlineClasses.Links import Organisational
        Link = Organisational()
        
        webbrowser.open(Link)
        speak("Please wait sir. Connecting you to Teams!")
        sleep(20)
        click(x=1225, y=512)
        sleep(39)
        click(x=772, y=684)
        sleep(2)
        click (x=1011, y=681)
        sleep(2)
        click (x=1102, y=618)        
        speak("Joining Manohar sir's class!")
   
    elif "economics" in Subject:
        from OnlineClasses.Links import Economics
        Link = Economics()
        
        webbrowser.open(Link)
        speak("Please wait sir. while i Connect you to Teams!")
        sleep(20)
        click(x=1225, y=512)
        sleep(39)
        click(x=772, y=684)
        sleep(2)
        click (x=1011, y=681)
        sleep(2)
        click (x=1102, y=618)
        
        speak("Joining Vinod sir's class")

    elif "coding" in Subject:
        from OnlineClasses.Links import Economics
        Link = Economics()
        
        webbrowser.open(Link)
        speak("Please wait sir. while i Connect you to Teams!")
        sleep(20)
        click(x=1225, y=512)
        sleep(39)
        click(x=772, y=684)
        sleep(2)
        click (x=1011, y=681)
        sleep(2)
        click (x=1102, y=618)
        
        speak("Joining Vinod sir's class")
    
    elif "prime" in Subject:
        from OnlineClasses.Links import Tally
        Link = Tally()
        
        webbrowser.open(Link)
        speak("Please wait sir. Connecting you to Teams!")
        sleep(20)
        click(x=1225, y=512)
        sleep(39)
        click(x=772, y=684)
        sleep(2)
        click (x=1011, y=681)
        sleep(2)
        click (x=1102, y=618)
        
        speak("Joining Warden sir's class!.")
    
    elif "second" in Subject:
        from OnlineClasses.Links import Add
        Link = Add()
        
        webbrowser.open(Link)
        speak("Please wait sir. Connecting you to Teams!")
        sleep(20)
        click(x=1225, y=512)
        sleep(39)
        click(x=772, y=684)
        sleep(2)
        click (x=1011, y=681)
        sleep(2)
        click (x=1102, y=618)
        speak("Joining additional english class sir!")
        
  
    

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-ind")
        print(f"You said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:        
        query = takeCommand().lower()

          
        if 'wikipedia' in query:
           speak('searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
                        
        elif 'open instagram' in query:
            speak("Opening instagram, please wait sir!")
            webbrowser.open("instagram.com")
        elif "attendance" in query:
            speak ("opening L.M.S. attendance page!")
            webbrowser.open("https://lms.sssihl.edu.in/mod/attendance/view.php?id=48524")
            sleep(10)
            click(x=1311, y=471)
        elif "feeling" in query:
            speak("do you want me to play some music ?")
        elif 'please' in query:
            speak("opening VLC player")
            music_dir = 'E:\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(f"Sir, the time is {strTime}")
        #elif "next" in query:
            sleep(2)
            click(x=107, y=1010)

        elif "whatsapp message" in query:
            
            name = query.replace("whatsapp message ","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            speak(f"what you want to send {Name}")
            MSG = takeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif "text" in query:
            speak ("With whom ?")
            name = takeCommand()
            from Automations import WhatappChat
            WhatappChat(name)




  
    
        elif "online" in query:
            
            from jarvis import OnlineClass
            speak("Tell me the subject name sir!")
            
            Class = takeCommand()
            
            OnlineClass(Class)
                  


        elif 'break' in query:
            speak("Ok Sir , You can call me anytime !")
            speak('Just say Hello Susan!')
            break
        