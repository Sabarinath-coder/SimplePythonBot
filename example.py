import pyttsx3

speaker=pyttsx3.init()
voices=speaker.getProperty('voices')
speaker.setProperty('voice',voices[0].id)
speaker.say("hello")
speaker.runAndWait()