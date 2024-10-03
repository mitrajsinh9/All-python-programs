import speech_recognition as sr

r = sr.Recognizer()

print("Please talk")

with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)  # Increased duration for better capture
    print("Recognizing.....")

    try:
        text = r.recognize_google(audio_data).lower()  # Convert to lower case for uniform comparison
        print(f"You said: {text}")

        if text == "hello":
            print("How are you?")
        elif text == "how are you":
            print("I am fine, thank you!")
        elif text == "hungry":
            print("Let's eat something. What do you have in mind?")
        elif text == "what is the time":
            from datetime import datetime

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"The current time is {current_time}")
        elif text == "what is the date":
            from datetime import datetime

            today = datetime.now()
            current_date = today.strftime("%Y-%m-%d")
            print(f"Today's date is {current_date}")
        elif text == "tell me a joke":
            print("Why don't scientists trust atoms? Because they make up everything!")
        elif text == "what is the weather":
            print("I can't check the weather right now, but you can check your local weather app.")
        elif text == "play music":
            print("I can’t play music right now, but you can use a music app to enjoy some tunes.")
        elif text == "open calculator":
            import os

            os.system("calc")  # For Windows, use 'calc' or 'gnome-calculator' for Linux
            print("Opening calculator...")
        elif text == "set an alarm":
            print("I can’t set an alarm right now, but you can use your phone or computer to set it.")
        elif text == "goodbye":
            print("Goodbye! Have a great day!")
        else:
            print("Sorry, I didn't understand that.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")