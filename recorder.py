import sounddevice as sd
import soundfile as sf
import requests
import openai
import os
import tempfile

openai.api_key = os.getenv('OPENAI_API_KEY')

def record_audio():
    # Generate a unique filename using tempfile
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        filename = temp_file.name

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

        # Make API request
        url = "https://api.openai.com/v1/audio/transcriptions"
        api_key = openai.api_key
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        data = {
            "model": "whisper-1"
        }

        with open(filename, "rb") as audio_file:
            files = {
                "file": audio_file
            }

            response = requests.post(
                url,
                headers=headers,
                data=data,
                files=files
            )

        # Check for errors in the response
        if response.status_code != 200:
            print("Error:", response.text)
            return None

        try:
            transcription = response.json()["text"]
            return transcription
        except KeyError:
            print("Error: Failed to retrieve transcription from response.")
            print("Full response:", response.json())
            return None

if __name__ == "__main__":
    record_audio()
