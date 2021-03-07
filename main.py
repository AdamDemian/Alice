import speech_recognition as sr

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as sourse:
        print("Povec niečo")
        audio = r.listen(sourse)
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("Prepáč nerozumela som.")
        except sr.RequestError:
            print("Sorry, my speach server is down.")
