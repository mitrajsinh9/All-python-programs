import pyaudio

# Initialize the mixer module
pyaudio.mixer.init()

# Load your MP3 file
pyaudio.mixer.music.load("Aaj Ki Raat - Stree 2 128 Kbps.mp3")

# Play the MP3 file
pyaudio.mixer.music.play()