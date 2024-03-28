import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import pyaudio
import wolframalpha
import webbrowser
import os
import random
import smtplib
import pyjokes
import winshell
import subprocess


engine=pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#wish function:
#it is used to greet the user and introduce itself   
#for greeting and intro   

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<17:
        speak("good afternoon!")
    elif hour>=17 and hour<21:
        speak("good evening!")
    else:
        speak("good night!")
    speak("I am friday    Please tell me how may I help you")
 
 
 #command function:
 #takes command from the user and converts that into a string   
        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=2)
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=10000
        
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    
    
    except Exception as e:
        print("could you please say that again...")
        return "none"                       
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sheechan1525@gmail.com','1234567')
    server.sendmail('chanshe1525@gmail.com',to,content)
    server.close()
        
   
#main function:
#it checks the commands given by the user and performs the actions respectively

if __name__=="__main__" :
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching in wikipedia...')
            query = query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'google' in query:
            speak("opening google")
            webbrowser.open("google.com")
            
        elif 'open bing' in query:
          speak('Opening Bing')
          webbrowser.open("bing.com")
          
     
        elif 'stack' in query:
          speak("Opening StackOverflow")
          webbrowser.open("stackoverflow.com")
          
     
        elif 'i love you' in query:
            speak("i love you too  ")
            
        elif 'joke' in query:

          speak(pyjokes.get_joke())
            
        elif 'play song'  in query:
            music_dir='C:\\Users\\irann\\Music\\iTunes\\songs'
            songs =os.listdir(music_dir)
            print(songs)
            d=random.choice(songs)
            os.startfile(os.path.join(music_dir,d))
            
        elif 'email Badri' in query:
            try:
                speak("what should be the content")
                content=takeCommand()
                to = "chanshe1525@gmail.com"
                sendemail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir couldnt send the email")
                    
        elif 'who are you' in query:
            speak("i am edith.  i am your desktop voice assisstant")
            
        elif 'exit' in query:
          speak("In a moment, sir")
          exit()
          
        elif 'empty recycle bin' in query:
          winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
          speak("Recycle Bin emptied sir")
          
          
        elif "restart" in query:
          speak("Please Provide Confirmation")
          x = takeCommand().lower()
          if x == "confirm  restart":
               speak("Restarting Computer")
               subprocess.call(["shutdown", "/r"])
          else:
               pass

        elif 'shutdown system' in query:
          speak("Please Provide Confirmation")
          x = takeCommand().lower()
          if x == "confirm system shutdown":
               speak("Shutting Down computer")
               subprocess.call(["shutdown", "/s"])
               
        
          
       
          
        
        
            
        
        

    



 
    
    

    