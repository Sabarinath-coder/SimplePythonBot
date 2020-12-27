import speech_recognition

earings=speech_recognition.Recognizer()  

with speech_recognition.Microphone() as source:
    print("listening....")  
    earings.adjust_for_ambient_noise(source)
    voice=earings.listen(source)            
    text=earings.recognize_google(voice)
    print(text)                            
