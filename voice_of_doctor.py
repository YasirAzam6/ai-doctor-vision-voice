
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):

    language = 'en'

    audioobject = gTTS(
        text=input_text,
        lang=language,
        slow=False
        )
    audioobject.save(output_filepath)


import os
from elevenlabs import ElevenLabs

# Initialize ElevenLabs client
client = ElevenLabs(
    api_key = ("sk_0019d536f5ca0e062e5af55ca077669264bde3e2c9393acb")
)

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    audio_stream = client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL",  # You can replace this with another valid voice_id
        model_id="eleven_multilingual_v1",
        text=input_text
    )

    # Combine audio chunks
    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    print(f"Audio saved to: {output_filepath}")

import subprocess
import platform
from pydub import AudioSegment

def text_to_speech_with_gtts(input_text, output_filepath):

    language = 'en'

    audioobject = gTTS(
        text=input_text,
        lang=language,
        slow=False
        )
    audioobject.save(output_filepath)
    # conversion frmo wav to mp3
    sound = AudioSegment.from_mp3("gtts_autoplay_testing.mp3")
    sound.export(output_filepath, format="wav")

    os_name = platform.system()
         
    try:
        if os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}" ).PlaySync();'])
        else:
            raise OSError("Unsupported OS for audio playback.")
    except Exception as e:
        print(f"Error playing audio: {e}")

input_text = "Hello, this is a test of the text to speech conversion using gTTS new version."



####################################################################################################################################
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    audio_stream = client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL", 
        model_id="eleven_multilingual_v1",
        text=input_text
    )

    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    sound = AudioSegment.from_mp3(output_filepath)
    sound.export(output_filepath, format="wav")
    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}" ).PlaySync();'])
        else:
            raise OSError("Unsupported OS for audio playback.")
    except Exception as e:
        print(f"Error playing audio: {e}")

    print(f"Audio saved to: {output_filepath}")