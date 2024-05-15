import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error recognizing your speech.")
            return ""

def main():
    speak("Hello, I am naruto, your virtual assistant. How can I assist you today?")
    while True:
        query = listen()
        if "hello" in query:
            speak("Hello! How can I help you?")
        elif "how are you" in query:
            speak("I'm doing well, thank you for asking.")
        elif "what's the time" in query:
            speak("The current time is 10:30 AM.")
        elif "tell me a joke" in query:
            speak("Why don't scientists trust atoms? Because they make up everything!")
        elif "weather" in query:
            speak("The weather today is partly cloudy with a high of 75 degrees Fahrenheit.")
        elif "news" in query:
            speak("Here are the latest headlines...")
            speak("That's all for now. How else can I assist you?")
        elif "set a reminder" in query:
            speak("What would you like to set a reminder for?")
        elif "send email" in query:
            speak("Who would you like to send an email to?")
        elif "take a note" in query:
            speak("Sure, what would you like to take a note of?")
        elif "tell me about yourself" in query:
            speak("I am naruto, your virtual assistant, designed to help you with various tasks and provide information.")
        elif "open calculator" in query:
            speak("Opening calculator.")
        elif "search" in query:
            speak("What would you like me to search for?")
        elif "tell me a fact" in query:
            speak("Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!")
        elif "bye" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
