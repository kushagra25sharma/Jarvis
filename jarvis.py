import pyttsx3 #text to speach conversion library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib # defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener
#smtp: simple mail transfer protocol


chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


# to use inbuilt voice of the computer 
engine = pyttsx3.init('sapi5') #constructs a new TTS engine (A TTS Engine converts written text to a phonemic representation, then converts the phonemic representation to waveforms that can be output as sound.)
# sappi5 is microsoft speech api, the technology for voice recognition and synthesis
voices = engine.getProperty('voices') # gives the array of voices available
engine.setProperty('voice', voices[0].id) # we are setting the voice property to the voice present at 1 index


def speak(audio):
    engine.say(audio)#queues a command to speak an utterance
    engine.runAndWait() # blocks while processing all queued command. Returns when queue is emptied


def welcome():
    # function will greet me whenver I will start the application
    curHour = int(datetime.datetime.now().hour)

    if curHour >= 0 and curHour < 12:
        speak("Good morning!")
    elif curHour >= 12 and curHour < 17:
        speak("Good afternoon!")        
    else :
        speak("Good evening!")    

    speak("I am Jarvis. How may I help you?")    


def  takeCommand():
    # this function will take microphonic input from the user and will return string output

    recognizer = sr.Recognizer() # Creates a new ``Recognizer`` instance, which represents a collection of speech recognition functionality.
    with sr.Microphone() as source: # Creates a new Microphone instance, which represents a physical microphone on the computer we named it source
        print("Listening...")
        recognizer.pause_threshold = 1 # no of seconds it will wait in non-speaking interval before a phrase is considered completed
        audio = recognizer.listen(source) # Records a single phrase from source (an AudioSource instance) into an AudioData instance, which it returns.

    try:
        print("Recognizing...")  # recognizes what we said using google's api  
        query = recognizer.recognize_google(audio, language='en-in') # Performs speech recognition on audio_data (an AudioData instance), using the Google Speech Recognition API.
        print(f"Kushagra: {query}\n")

    except Exception as e:
        print(e)  
        print("Say that again.")      
        return "None" # returning string "None"

    return query    


def sendEmail(message, to):
    server = smtplib.SMTP("smtp.gmail.com", 587)# to do smtp auth with TLS (Transport Layer Security is an encryption protocol that protects Internet communications.) we have to use port 587
    server.ehlo() # Identify yourself to an ESMTP (extended simple mail transfer protocol) server
    server.starttls() # It offers a way to upgrade a plain text connection to an encrypted (TLS or SSL) connection instead of using a separate port for encrypted communication
    server.login("your_gmail_id here", "password here")# logins you to your mail account
    server.sendmail("your_gmail_id here", to, message) # sends mail
    server.close() # closing the connection


if __name__ == "__main__":
    welcome()
    while True:
        query = takeCommand().lower()

        # logics for querries :-
        if "wikipedia" in query:
            speak("Searching results, one moment please...")
            query = query.replace("wikipedia", "")

            try:
                result = wikipedia.summary(query, sentences=1)
                print(result)
                speak(result)

            except Exception as e:
                print(e)
                speak("Sorry not able to process the results at the moment")

        
        elif "search for" in query:
            speak("Fetching results from the web.")
            query = query.replace("search for ", "")
            webbrowser.get(chrome_path).open("www.google.com/search?q=" + query)


        elif "open youtube" in query:
            speak("opening you tube in a second")
            webbrowser.get(chrome_path).open("youtube.com")


        elif "open gmail" in query:
            speak("opening mail, one moment please")
            webbrowser.get(chrome_path).open("gmail.com")


        elif "open codeforces" in query:
            speak("opening codeforces in few moments")    
            webbrowser.get(chrome_path).open("codeforces.com")


        elif "open vs code" in query:
            speak("opening vs code")
            filePath = "C:/Users/acer/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(filePath)


        elif "play music" in query:
            speak("playing music for you")
            webbrowser.get(chrome_path).open("www.youtube.com/watch?v=PqFMFVcCZgI")
            # musicPath = 
            # songs = os.listdir(musicPath)
            # print(songs)
            # index = random.randrange(0,songs.len())
            # os.startfile(os.path.join(musicPath, songs[index]))


        elif "send email to" in query:
            try:
                speak("What should be the message?")
                message = takeCommand()
                to = ""
                sendEmail(message, to)
                speak("Email successfully send!")

            except  Exception as e:
                print(e)
                speak("Sorry can't send the email at the moment.")
            
        
        elif "open zoom" in query:
            speak("Opening zoom app")
            filePath = "C:/Users/acer/AppData/Roaming/Zoom/bin/Zoom.exe"
            os.startfile(filePath)


        elif "go to sleep" in query:
            speak("I am going to sleep now.")             
            exit()



