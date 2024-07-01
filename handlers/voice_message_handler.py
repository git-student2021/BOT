from create_bot import bot
from pathlib import Path
from aiogram.types import ContentType, File, Message

async def handle_file(file_name: str, file_id: str, path: str):
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"{path}{file_name}.mp3")