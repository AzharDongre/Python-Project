import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import googlesearch
import smtplib
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("voice at your service sir!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        Query=r.recognize_google(audio, language='en-in')
        print("User said: ",Query)


    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return Query



def sendEmail(to,content):
    f1=open("file.txt","r")
    lines=f1.readlines()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('azhardongre786@gmail.com',lines)
    server.sendmail("azhardongre786@gmail.com",to,content)
    server.close()
    f1.close()





if __name__ == "__main__":
    wishMe()
    while(1):
        Query=takeCommand().lower()

    
        if 'wikipedia' in Query:
            speak("searching wikipedia...")
            Query=Query.replace("wikipedia","")
            results=wikipedia.summary(Query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        if 'search in google' in Query:
            try:
                from googlesearch import search
            
            except ImportError:
                print("No module named 'google' found")

            
            Query=Query.replace("googlesearch","")
            for results in search(Query,tld="co.in",num=10,stop=1,pause=2):
                speak("According to Google")
                print(results)
                speak(results)


        elif 'open youtube' in Query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in Query:
             webbrowser.open("facebook.com")

        elif 'open google' in Query:
             webbrowser.open("google.com")

        elif 'open google chrome' in Query:
            webbrowser.open("google chrome.com")

        elif 'play some music' in Query:
            music_dir = 'D:\\songs'
            songs=random.choice(os.listdir(music_dir))        
            os.startfile(os.path.join(music_dir,songs))

        elif 'how many songs' in Query:
            music_dir='D:\\songs'
            songs=os.listdir(music_dir)
            cnt=0
            for x in songs:
                cnt=cnt+1
            print(cnt)
            speak(f"you have {cnt} songs")
            


        elif 'for today' in Query:
            speak("anytime sir!!")
            exit(0)

        elif 'the time' in Query:
            strtime=datetime.datetime.now().strftime("%H:%M:%M")
            print("Sir,the time is :")
            speak("Sir. The time is")
            print(strtime)
            speak(strtime)

      
        elif 'play video' in Query:
            video_dir='D:\\Videos'
            Videos=random.choice(os.listdir(video_dir))
            os.startfile(os.path.join(video_dir,Videos))



        elif 'play movie' in Query:
            movie_dir='D:\\Movies'
            movies=random.choice(os.listdir(movie_dir))
            os.startfile(os.path.join(movie_dir,movies))

        elif 'how many movies' in Query:
            movie_dir='D:\\Movies'
            movies=os.listdir(movie_dir)
            count=0
            for x in movies:
                count=count+1
            print(count)
            speak(f"you have {count} movies")
        

        
        elif 'about you' in Query:
            print("I am Voyce. An simple AI created by Mr.Azhar and Miss Sanika ")
            speak("I am voice. An simple AI. Created by Mr. Azhar and Miss Sanika")

        elif 'hello voice' in Query:
            #print("hello there!!")
            speak("hello there!!")

        elif 'how are you' in Query:
            speak("I am doing great. Thankyou for asking")
        

        
        elif 'your birth date' in Query:
            speak("I was created on 4/4/2020")
                             
        elif 'do for me' in Query:
            print("You can tell me to open facebook,google,Youtube,search info in wikipedia,play music,play movies,ask me time etc")
            speak("You can tell me to open facebook. Google. Youtube. Search info in wikipedia. Play music. Play movies etc")
    

        elif 'good morning' in Query:
            speak("a very good morning to you too!!")
            speak("Did you sleep well?")
            if 'yes' in Query:
                speak("That sounds good!!")

        elif 'that will be all' in Query:
            speak("My pleasure sir")
            exit(0)

        elif 'joke' in Query:
            speak(pyjokes.get_joke)

        elif 'make a note' in Query:
            speak("What should i write,sir")
            note=takeCommand()
            file=open("note.txt","w")
            speak("Sir, should i include date and time")
            snfm=takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(note)
                speak("note is made successfully")
            else:
                file.write(note)
                speak("note is made successfully")


        elif 'show note' in Query:
            speak("showing notes")
            file=open("notes.txt","r")
            print(file.read())
            speak(file.readlines())

        elif 'send email to' in Query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="azhardongre786@gmail.com"
                sendEmail(to,content)
                speak("the email has been sent sir")
                print("the email has been sent sir")
            except Exception as e:
                print(e)
                speak("sorry sir. I am not able to send this email")
                    
        elif 'temperature' in Query:  

            search = "temperature in mahableshwar"
            url=f"https://www.google.com/search?q{search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")
