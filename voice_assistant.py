import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")

# Function to take commands from the user
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
    
    return command.lower()

# Function to perform a task based on the command
def perform_task(command):
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace('wikipedia', '')
        result = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        speak(result)

    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif 'time' in command:
        time_str = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time_str}")

    elif 'play music' in command:
        music_dir = '/path/to/your/music'  # Set the correct path to your music folder
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music")

    elif 'open code' in command:
        code_path = "/path/to/your/code/editor"  # Set the correct path for your code editor
        os.startfile(code_path)
        speak("Opening your code editor")

    elif 'shutdown' in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 1")

    elif 'exit' in command or 'quit' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I can search that on Google")
        webbrowser.open(f"https://www.google.com/search?q={command}")

#### Step 3: Putting It All Together

# Now, let’s integrate everything into a main loop so that your assistant can continuously listen to commands and respond accordingly:

# ```python
def main():
    greet_user()
    while True:
        command = take_command()
        if command == "none":
            continue
        perform_task(command)

if __name__ == "__main__":
    main()
