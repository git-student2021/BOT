from pathlib import Path
from openai import OpenAI
from decouple import config
# client = OpenAI()

def ttv(text, file_id, path):

    client = OpenAI(api_key=config('OPENAI_API_KEY'))

    speech_file_path =  f"{path}{file_id}.mp3"
    response = client.audio.speech.create(
      model="tts-1",
      voice="alloy",
      input= f"{text}"
    )

    response.stream_to_file(speech_file_path)

    return speech_file_path