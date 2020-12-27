import speech_recognition
import datetime
import pyttsx3
import wikipedia
import pywhatkit

speaker=pyttsx3.init()
voices=speaker.getProperty('voices')
speaker.setProperty('voice',voices[0].id)

def talk(text):
    speaker.say(text)
    speaker.runAndWait()

def get_text():
    try:
        earings=speech_recognition.Recognizer()  

        with speech_recognition.Microphone() as source:
            print("listening....")  
            earings.adjust_for_ambient_noise(source)
            voice=earings.listen(source)            
            text=earings.recognize_google(voice)
            print(text)
            return text 
    except:
        talk("please say the command again")





def main():
    try:
        command=get_text()

        if "what is your name" in command:
            talk("my name is raam")
        elif "how are you" in command:
            talk("iam fine")
      
        elif 'time' in command:
            time=datetime.datetime.now().strftime("%I:%M %p")
            print("Current time:",time)
            talk(time)
        elif 'date' in command:
            date=datetime.datetime.now().strftime("%d/%B/%Y")
            print("current date:",date)
            talk(date)
        elif 'who' in command:
            person=command.replace('who','')
            info=wikipedia.summary(person,1)
            print(info)
            talk(info)
        elif 'play' in command:
            song=command.replace('play','')
            print("playing "+song+'.....')
            talk('ya iam playing')
            pywhatkit.playonyt(song)
        
    except:
        talk("please say the command again")
    
while True:
    main()