import speech_recognition
import pyttsx3

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def get_text():
    earings=speech_recognition.Recognizer() # listner 

    with speech_recognition.Microphone() as source:
        print("listening......") #hearing voice through microphone 
        earings.adjust_for_ambient_noise(source) # for adjust the voice
        voice=earings.listen(source)             # This is the correct voice
        text=earings.recognize_google(voice)     # this command convert the voice to text
        
        return text

def talk(text):
    engine.say(text)
    engine.runAndWait()

def run():
    command=get_text()

    if "what is your name" in command:
        talk("my name is raam")
run()
