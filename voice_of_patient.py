import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def record_audio(file_path, timeout=100, phrase_time_limit=100):
    """
    Records audio from the microphone and saves it to a file.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("adjustments for clear voices...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start Speaking now...")
            
            #converting  the audio file into an MP3 file
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording finished.")

            #now converting the record audio to an  mp3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"Audio saved to {file_path}")

    except sr.WaitTimeoutError:
        logging.error(f"An error occured: {e}")
audio_filepath = "patient_voice.mp3"
record_audio(file_path = audio_filepath)


# Setting up the speech to text-SST model for transcription

import os
from groq import Groq
#import whisper

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
sst_model = "whisper-large-v3"

def transcribe_with_groq(audio_filepath, sst_model,GROQ_API_KEY):
 
    client = Groq(api_key=GROQ_API_KEY)
    audio_file = open(audio_filepath, "rb")
    transcription = client.audio.transcriptions.create(
        model=sst_model,
        file=audio_file,
        language="en",
    )

    return transcription.text




    #officee
    # microphone = sr.Microphone()

    # with microphone as source:
    #     print("Please speak something...")
    #     audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

    # with open(file_path, "wb") as audio_file:
    #     audio_file.write(audio.get_wav_data())

