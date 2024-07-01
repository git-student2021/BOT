from openai import OpenAI
from decouple import config
import os
import json
from converter.voice_converter import vtt
from pathlib import Path

def request_GPT(text):
        client = OpenAI(api_key=config('OPENAI_API_KEY'))

        assistant = client.beta.assistants.create(
            name="Bot assistent",
            instructions="You are a personal assistent. Answer questions briefly, in a sentence or less.",
            model="gpt-4-1106-preview",
        )

        thread = client.beta.threads.create()

        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content = text
        )

        messages = client.beta.threads.messages.list(thread_id=thread.id)

        run = client.beta.threads.runs.create_and_poll(
          thread_id=thread.id,
          assistant_id=assistant.id,
          instructions="Please help a user."
        )

        if run.status == 'completed':
          messages = client.beta.threads.messages.list(
            thread_id=thread.id
          )

          data = dict(json.loads(messages.model_dump_json()))

          print(data['data'][0]['content'][0]['text']['value'])
          return data['data'][0]['content'][0]['text']['value']
        else:
          print(run.status)
          return run.status