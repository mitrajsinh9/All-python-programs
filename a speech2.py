import speech_recognition as sr
r=sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:
    audio_data=r.record(source,duration=2)
    print("Recognizing.....")
    text=r.recognize_google(audio_data)
    print(text)
    if text == "hello":
        print("how are you?")
    elif text == "how are you":
        print("I am fine")
    elif text == "hungry":
        print("Let's eat something")
