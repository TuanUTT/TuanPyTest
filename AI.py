from os import curdir
import pyttsx3
import speech_recognition
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot:...")
        
    try : 
        you = robot_ear.recognize_google(audio)
    except :
        you = ""
    print("You: " + you)
    if you == "":
        robot_brain = "hello eri, wake up!"
    elif "hello" in you:
        robot_brain = "Hi, How are you today"
    elif "bye" in you:
        robot_brain = "bye bye"
    elif "what is your name?" in you:
        robot_brain = "My name is Robot-AI"
    elif "I'm fine, thank you. And you" in you:
        robot_brain = "I'm ok because i can say with you"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif you == "time":
        now = datetime.now()
        robot_brain = now.strtime("%H hours %M minutes %S seconds")
    elif you == "Aiss":
        robot_brain = "Why are you so boring today?"
    elif "bye" in you:
        robot_brain = "Bye Bye"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    
    print("Robot: "+robot_brain)
    voices = robot_mouth.getProperty('voices')
    robot_mouth.setProperty('voice', voices[1].id)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    robot_mouth.stop()
