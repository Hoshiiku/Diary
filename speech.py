import speech_recognition as sr
import pyaudio

audio_file = sr.Recognizer()
def audio_capture():
    with sr.Microphone() as audio:
        print("Say something")
        audio_file.adjust_for_ambient_noise(audio)
        file = audio_file.listen(audio)


    return file

def translate_to_spanish(file):
    try:
        text = audio_file.recognize_google(file, language ="es-ES")
        return text
    except:
        return "Couldn't understand the audio"
    

adui = audio_capture()
print(translate_to_spanish(adui))