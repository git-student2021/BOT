import types
import uuid
from pathlib import Path
from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, File

from create_bot import bot
from .voice_message_handler import handle_file
from converter.voice_converter import vtt #, vtt2
from request_GPT.req_gpt import request_GPT
from voice_answer.voice_generator import ttv
start_router = Router()
from aiogram.types import FSInputFile
from aiogram.methods.send_voice import SendVoice


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')


@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')


@start_router.message(F.text.contains('id'))
async def cmd_message_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Твой ID: {message.from_user.id}")


@start_router.message(F.content_type.in_({'text'}))
async def text_message_handler(message: Message):
    await message.answer(f"Очень интересное текстовое сообщение!")


@start_router.message(F.content_type.in_({'voice'}))
async def voice_message_handler(message: Message):
    file_id = message.voice.file_id
    path = "./audio_msg/"

    await handle_file(file_id=f"{file_id}", file_name=f"{file_id}", path=path)
    print(path + file_id + ".mp3")
    text_voice = vtt(f"{path}{file_id}.mp3")
    respons_GPT = request_GPT(text_voice)
    respons_file_path = ttv(text=respons_GPT, file_id=file_id, path="./audio_msg/audio_answer/")
    print(respons_file_path)
    voice_file = types.FSInputFile(respons_file_path)
    await message.answer_voice(voice_file)





@start_router.message()
async def unknown_message_handler(message: Message):
    await message.answer(f'получено странное сообщение {message.content_type}')