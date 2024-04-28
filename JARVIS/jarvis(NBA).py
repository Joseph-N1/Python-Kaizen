import datetime
import pyttsx3
import speech_recognition as sr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import webbrowser
import wikipedia
import logging
import sys
import keyboard  # This library is used to check for key presses

# Setup logging
logging.basicConfig(level=logging.INFO)

# Environment variables for email
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'youremail@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your-password')

# Engine initialization and configuration
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)  # Speed of speech

# Recognizer initialization
recognizer = sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning! I am Jarvis Sir. How may I assist you?")
    elif hour < 18:
        speak("Good afternoon! I am Jarvis Sir. How may I assist you?")
    else:
        speak("Good evening! I am Jarvis Sir. How may I assist you?")

def listen():
    # List available microphones for diagnostics
    print("Available microphones:", sr.Microphone.list_microphone_names())
    
    try:
        # You might need to specify the device_index if the default microphone is not correct
        with sr.Microphone() as source:
            print("Microphone is open.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Adjusted for ambient noise.")
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Audio received, processing...")
            return recognizer.recognize_google(audio, language='en-us').lower()
    except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
        speak("I couldn't understand. Please try again.")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        speak("An unexpected error occurred. Please try again.")
        return None

def send_email(to, content):
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = to
    message['Subject'] = 'Notification from Jarvis'
    message.attach(MIMEText(content, 'plain'))
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
            speak("Email has been sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send email. Error: {e}")
        speak("I am not able to send this email right now.")

def execute_command(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        results = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
        speak("According to Wikipedia, " + results)
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
    elif 'open stack overflow' in query:
        webbrowser.open("https://stackoverflow.com")
    elif 'play music' in query:
        music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {str_time}")
    elif 'open code' in query:
        code_path = r"C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
    elif 'email to john' in query:
        speak("What should I say?")
        content = listen()
        if content:
            send_email("john@example.com", content)


def execute_command(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        results = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
        speak("According to Wikipedia, " + results)
    elif 'nba schedule' in query:
        speak("Fetching NBA schedules for 2024...")
        schedules = fetch_nba_schedules("2024")
        if schedules:
            for game in schedules[:5]:  # Just speak about the first 5 for brevity
                speak(f"{game['AwayTeam']} at {game['HomeTeam']} on {game['Day']}")
        else:
            speak("No NBA schedule information available.")
    elif 'nba injuries' in query:
        speak("Fetching information on injured NBA players...")
        injuries = fetch_injured_players()
        if injuries:
            for injury in injuries[:5]:  # Limit to 5 to keep the response brief
                speak(f"{injury['Name']} from {injury['Team']} is currently injured.")
        else:
            speak("No injury information available.")
    elif 'nba standings' in query:
        speak("Fetching NBA standings for 2024...")
        standings = fetch_standings("2024")
        if standings:
            for team in standings[:5]:  # Limit to top 5 teams
                speak(f"{team['Name']} is ranked {team['Rank']} with {team['Wins']} wins and {team['Losses']} losses.")
        else:
            speak("No standings information available.")
    elif 'shutdown' in query:
        speak("Shutting down, goodbye!")
        sys.exit(0)
    # Add other commands as needed


def main():
    wish_me()
    error_count = 0
    while True:
        if keyboard.is_pressed('esc'):
            speak("Escape key pressed, shutting down. Goodbye!")
            break
        query = listen()
        if query:
            if any(ext in query for ext in ['shutdown', 'stop', 'exit', 'quit']):
                speak("Shutting down, goodbye!")
                break
            execute_command(query)
        else:
            error_count += 1
            if error_count >= 10:
                speak("Too many errors, I am shutting down. Goodbye!")
                break

if __name__ == "__main__":
    main()
