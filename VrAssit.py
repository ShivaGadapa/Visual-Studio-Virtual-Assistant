# importing speech recognition package from google api
import os  # to save/open files

import keyboard as kb
import playsound  # to play saved mp3 file
import speech_recognition as sr
from gtts import gTTS  # google text to speech
from selenium import webdriver  # to control browser operations
import time as wt
import pyautogui as ag

num = 1
global status

def assistant_speaks(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print("VirAsst : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3 "
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)

# Listen Back to user to continue on same context()
def listen_back(): 
    while(1):
        text = get_audio().lower()
        wt.sleep(1)

        if text == 0: 
            continue
        elif "good" in str(text):
            assistant_speaks("Ok then, I will wait for your next command")
            wt.sleep(10)
        elif "exit" in str(text):
            assistant_speaks("Ok, Closing Visual Studio")
            kb.press_and_release('alt + F4')
            break
        else:
            Vs_Project(text)
    
# Visual Studio project creation
def Vs_Project(input):
    if "create" in input or "project" in input:
        kb.press_and_release('ctrl + shift + n')
        assistant_speaks("Ok, what kind of project")
        listen_back()
    elif "Windows" in input or "console" in input:
        kb.press_and_release('ctrl + E')
        kb.write("windows console")
        ag.press('Tab')
        ag.press('Tab')
        ag.press('Tab')
        assistant_speaks("Ok, Please Name the Project")
        listen_back()
    elif "apple" in input:
        ag.write('apple')
        assistant_speaks("Plese confirm Yes or No")
        listen_back()
    elif "yes" in input:
        ag.press('enter') #Enter key
        assistant_speaks("Congratulations, Console App created")
        listen_back()
    elif "no" in input:
        ag.press('esc') #Esc Key
        assistant_speaks("Ok, what's next")
        listen_back()
    


# function used to open application 
# present inside the system. 
def open_application(input): 

    if "visual studio" in input: 
        assistant_speaks("Opening VisualStudio 2017") 
        os.startfile('C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\Professional\\Common7\\IDE\\devenv.exe')
        wt.sleep(4)
        assistant_speaks("Ok, whats next")
        listen_back() #Listens Back to User
        return

    elif "word" in input: 
        assistant_speaks("Opening Microsoft Word") 
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk') 
        return

    else:
        assistant_speaks("Application not available") 
        return     

def process_text(input): 
    
    try: 
        if 'search' in input or 'play' in input: 
            # a basic web crawler using selenium 
            #search_web(input) 
            return

        elif "who made you" in input or "created you" in input: 
            speak = "I have been created by Shiva Prasad."
            assistant_speaks(speak) 
            return

        elif 'open' in input: 
            status = False  
            # another function to open  
            # different application availaible 
            open_application(input.lower())  
            return

        else: 
            assistant_speaks("I can search the web for you, Do you want to continue?")
    except : 

        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
        #ans = get_audio() 
        #if 'yes' in str(ans) or 'yeah' in str(ans): 
            #search_web(input)    



def get_audio(): 

    rObject = sr.Recognizer() 
    audio = '' 

    with sr.Microphone() as source: 
        print("Speak...") 
        
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)  
    print("Stop.") # limit 5 secs 

    try: 

        text = rObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        if text == 0:
            assistant_speaks("Am waiting for your response")
            listen_back()  
        return text 

    except: 

        assistant_speaks("Could not understand your audio, PLease try again !") 
        listen_back()
        return 0


# Driver Code 
if __name__ == "__main__": 
    name = "SHIVA"
    status = True
    wt.sleep(2)
    assistant_speaks("Welcome back, " + "Buddy" + '.')  
    while(1): 

        if status == True:
            assistant_speaks("What can i do for you ?") 
        else: 
            assistant_speaks("Ok, What is the next step ?")    
        text = get_audio().lower() 

        if text == 0: 
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistant_speaks("Ok bye, "+ name +'.') 
            break

        # calling process text to process the query 
        process_text(text)        
