import wolframalpha
client = wolframalpha.Client("lilpumpsaysnopeeking")

import wikipedia

import PySimpleGUI as sg
sg.theme('DarkBlue')
layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('JARVIS', layout)

import speech_recognition as sr

list = []

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        ques = "{}".format(text)
    except:
        print("Sorry could not recognize what you said")

import pyttsx3
engine = pyttsx3.init()

timer = 0

while True:
    try:
        wiki_res = wikipedia.summary(ques, sentences=2)
        wolfram_res = next(client.query(ques).results).text
        engine.say(wolfram_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(ques).results).text
        engine.say(wolfram_res)
        if timer == 1:
            break
        timer += 1
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(ques).results).text
        engine.say(wolfram_res)
        if timer == 1:
            break
        timer += 1
    except:
        wiki_res = wikipedia.summary(ques, sentences=2)
        engine.say(wiki_res)
        if timer == 1:
            break
        timer += 1

    engine.runAndWait()

    print (ques)

window.close()
