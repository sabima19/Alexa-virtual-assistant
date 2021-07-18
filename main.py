from subprocess import run
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')            
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
        return command   
    except:
        pass
    return ''
    


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        content=command.replace('what is','')
        info=wikipedia.summary(content,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'youtube' in command:
        talk('showing in youtube')
        pywhatkit.playonyt(command)
    elif 'you love' in command:
        talk('sorry i am already in a relationship')
    
    else:
        talk('Please say the command again.')
        run_alexa()
def repeat():
    talk("Do you want me to do or ask me anything ?say yes or no.")  
    print("Do you want me to do or ask me anything ?say yes or no")
    option=take_command()
    if 'yes' in option:
       print('yes')
       print('ok got it.Tell me')
       talk('ok got it tell me')
       run_alexa()
       repeat()

    else: 
         talk("thank you for using me")
         print("thank you for using me")

talk('Hello i am alexa')
print('Hello i am alexa')
talk('what i can do for you?')
print('what i can do for you?')
run_alexa()
repeat()
