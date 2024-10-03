import speech_recognition as sr
import emoji
r=sr.Recognizer()
text=""
c=1
while text!="no":
    print("Please talk and Say No for Stop")
    with sr.Microphone() as source:
        try:
            audio_data=r.record(source,duration=3)
            print("Getting",c)
            c+=1
            text=r.recognize_google(audio_data)
            print(text)
            if text=="no":
                print("bye")
            elif text=="face":
                print(emoji.emojize(':grinning_face:'))  # 😀
            elif text=="up":
                    print(emoji.emojize(':thumbs_up:'))             # 👍
        except:
            print("error")