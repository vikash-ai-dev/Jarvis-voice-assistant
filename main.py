import speech_recognition as sr
import webbrowser
import pyttsx3
import music

recognizer = sr.Recognizer()

def speak(text):
    print("Jarvis:", text)
    engine = pyttsx3.init()          
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()                   
    del engine                       
    

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1] 
        if song in music.music:
            speak("Playing " + song)
            webbrowser.open(music.music[song])
        else:
            speak("Sorry, I don't have that song.")  


if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        try:
            print("Recognizing....")

            with sr.Microphone() as source:
             
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=4)  

            command = recognizer.recognize_google(audio)
            print("You said:", command)

            if "jarvis" in command.lower():
                speak("Yes sir, I am lisetning.")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.2)
                    print("Jarvis Active....!")
                    audio = recognizer.listen(source, timeout=7, phrase_time_limit=5)
                    

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                processcommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Error:", e)

        except Exception as e:
            print("Other error:", e)

