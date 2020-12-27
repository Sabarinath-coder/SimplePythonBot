import pyttsx3
import speech_recognition
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
    except speech_recognition.UnknownValueError:
        talk("please say the command again")

def main():
    try:
        command=get_text()

        if "what is your name" in command:
            talk("my name is raam")
        elif "how are you" in command:
            talk("iam fine")
        elif "who is your creator" in command:
            talk("my creator is sabarinath")
    except TypeError:
        pass
while True:
    main()