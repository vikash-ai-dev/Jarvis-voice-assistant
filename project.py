import speech_recognition as sr
import webbrowser
import pyttsx3
import time

recognizer = sr.Recognizer()

def speak(text):
    print("Jarvis:", text)
    engine = pyttsx3.init()          # 
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()                
    del engine                      

def processcommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    else:
        speak("Sorry, I did not understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis")
    print("Jarvis Ready!")       
    time.sleep(1)

    while True:
        try:
            print("Listening for wake word....")

            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                print("Ready...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=4)

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("Yes sir, I am listening. Please give your command.")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.2)
                    print("Jarvis Active - Waiting for command....")
                    audio = recognizer.listen(source, timeout=7, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processcommand(command)

        except sr.WaitTimeoutError:
            print("Timeout, retrying...")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Network error:", e)

        except Exception as e:
            print("Error:", e)