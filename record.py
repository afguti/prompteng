import sounddevice as sd
import soundfile as sf

def record_audio(filename):
    # Open the audio file for writing
    with sf.SoundFile(filename, mode='w', samplerate=44100, channels=2) as file:
        # Callback function to write audio data to the file
        def callback(indata, frames, time, status):
            file.write(indata)
        
        # Specify the input device index (replace with the correct index number)
        input_device = 0

        # Start the audio recording
        with sd.InputStream(device=input_device, channels=2, callback=callback):
            print("Recording audio. Press Enter to stop...")
            input()  # Wait for the Enter key to be pressed
        
        print("Recording stopped.")

# Specify the filename to save the recorded audio
filename = "recorded_audio.wav"

# Start recording audio
record_audio(filename)

