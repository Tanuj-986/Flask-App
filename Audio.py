import sounddevice as sd
import numpy as np
import wave
import keyboard
import soundfile as sf



SAMPLERATE = 44100  
CHANNELS = 1        
OUTPUT_FILENAME = "prompt.wav"

def record_audio():
    print("Hold 'r' to start recording, release it to stop.")

    while True:
        keyboard.wait('r') 
        print("Recording started... Release 'r' to stop.")
        
        frames = [] 
        def callback(indata, frames_per_buffer, time_info, status):
            if status:
                print(status)
            frames.append(indata.copy()) 
        
        with sd.InputStream(samplerate=SAMPLERATE, channels=CHANNELS, dtype=np.int16, callback=callback):
            while keyboard.is_pressed('r'): 
                sd.sleep(100)

        print("Recording stopped.")

        
        audio_data = np.concatenate(frames, axis=0)

        
        with wave.open(OUTPUT_FILENAME, "wb") as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)  
            wf.setframerate(SAMPLERATE)
            wf.writeframes(audio_data.tobytes())

        print(f"Recording saved as '{OUTPUT_FILENAME}'")
        break  

# record_audio()



##################################################################################################



def play_audio(speed=1.0):

    # Read the audio file
    data, samplerate = sf.read("response.wav")

    # Adjust speed by resampling
    new_samplerate = int(samplerate * speed)  # Modify the sample rate
    sd.play(data, new_samplerate)  # Play audio at new sample rate
    
    sd.wait()  # Wait until playback finishes


# play_audio(speed=1.5)  # Play at 1.5x speed (faster)


