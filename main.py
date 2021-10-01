import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("i am Peenut, can i help you sir")  
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 100
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-US')
            print(f"user said: {query}\n")
        except Exception as e:
            print("say that again please...")
            return "None"
        return query        
                  
          



if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=8)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google translator' in query:
            webbrowser.open("https://translate.google.co.in/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open google map' in query:
            webbrowser.open("https://www.google.com/maps/@26.7438836,83.2827084,15z")  
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'open java point' in query:
            webbrowser.open("https://www.javatpoint.com/")
        elif 'open tutorials point' in query:
            webbrowser.open("https://www.tutorialspoint.com/index.htm")
        elif 'open geeksforgeeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")
        elif 'open Hacker rank' in query:
            webbrowser.open("https://www.hackerrank.com/")
        elif 'open github' in query:
            webbrowser.open("https://github.com/")
        elif 'open great learning' in query:
            webbrowser.open("https://www.greatlearning.in/?&utm_source=google&utm_medium=search&utm_campaign=Exact_Search_Application_Performance_Below24&adgroup_id=69790556391&campaign_id=1715209878&Keyword=great%20learning&placement=&utm_content=c&gclid=CjwKCAjw49qKBhAoEiwAHQVTo_diU2CyWCgjMXFyMHMTOlg6mmCuqE8ZaRK6C5hKmFQwKjrAQ3uE9BoCagAQAvD_BwE")
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 
        elif 'play music' in query:
            music_dir = 'D:\\Sangam\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}") 
        elif 'open vs code' in query:
            path_0 = "C:\\Users\\Ravita Prajapaty\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path_0) 
        elif 'open bracket' in query:
            Path_1 = "C:\\Program Files (x86)\\Brackets\\Brackets.exe"
            os.startfile(Path_1) 
        elif 'open xampp server' in query:
            path_2 = "C:\\xampp\\xampp-control.exe"
            os.startfile(path_2)
        elif 'open atom' in query:
            path_3 = "C:\\Users\\Ravita Prajapaty\\AppData\\Local\\atom\\atom.exe"
            os.startfile(path_3) 
        elif 'open anydesk' in query:
            path_4 = "C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"
            os.startfile(path_4)      

    
