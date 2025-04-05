from secret import *
from groq import Groq



######### STT #########



def STT(filename):
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3"
            )
    prompt = transcription.text
    
    print(prompt)
    return prompt


# STT()





#############   TTS   ############


def TTS(response, speech_file_path):
    # speech_file_path = "response.wav" 
    model = "playai-tts"
    voice = "Cillian-PlayAI"
    text = response
    response_format = "wav"

    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text,
        response_format=response_format
    )

    response.write_to_file(speech_file_path)


