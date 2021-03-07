import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as sourse:
    print("Povec niečo")
    audio = r.listen(sourse)
    voice_data = r.recognize_google(audio)
    print(voice_data)
