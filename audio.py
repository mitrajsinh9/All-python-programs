import pyaudio
import wave

# Parameters
WAVE_INPUT_FILENAME = "example.wav"  # Input file name

def play_audio(filename):
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open the WAV file
    with wave.open(filename, 'rb') as wf:
        # Open a stream for playback
        stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

        # Read and play audio in chunks
        chunk_size = 1024
        data = wf.readframes(chunk_size)
        while data:
            stream.write(data)
            data = wf.readframes(chunk_size)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

# Play the audio file
play_audio(WAVE_INPUT_FILENAME)
