import speech_recognition as sr
from time import ctime

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as sourse:
        audio = r.listen(sourse)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Prepáč nerozumela som.")
        except sr.RequestError:
            print("Sorry, my speach server is down.")
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        print("My name is Alice")
    if 'what time is it' in voice_data:
        print(ctime())


print("Ako ti môžem pomôcť?")
voice_data = record_audio()
print(voice_data)
respond(voice_data)
