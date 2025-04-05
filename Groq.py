import time
from Audio import record_audio, play_audio
from Brain import *
from secret import *
from STT_TTS import STT, TTS



def main():
    while True:
        method = input("Enter 1 for Text \n      2 for audio :- ")
    
        if method == "1":
            prompt = input("Enter Prompt: ")
            t1 = time.time()

        if method == "2":
            record_audio()
            t1 = time.time()
            prompt = STT()

        response = brain(prompt)

        TTS(response)

        t2 = time.time()

        t3 = t2-t1
        print(f"STT Response time: {t3}")

        # play_audio()
        break



if __name__ == "__main__":
    main()


