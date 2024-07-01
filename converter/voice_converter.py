from openai import OpenAI
from decouple import config
import os
import requests
import json


def vtt(path):
    client = OpenAI(
        api_key=config('OPENAI_API_KEY')
    )

    with open(path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    print(transcription.text)
    return transcription.text