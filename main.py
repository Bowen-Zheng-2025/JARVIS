import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening ...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '') # this replaces the word when you say it
        pywhatkit.playonyt(song)

run_jarvis()
