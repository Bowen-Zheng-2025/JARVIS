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

while True:
    event = ques
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(ques, sentences=2)
        wolfram_res = next(client.query(ques).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(ques).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(ques).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(ques, sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (ques)

window.close()
