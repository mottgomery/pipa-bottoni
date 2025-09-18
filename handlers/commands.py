from aiogram import Bot, Router, F
from aiogram.types import callback_query, Message
from aiogram.filters import CommandStart

import keyboards.inline_kb as in_kb
import handlers.function as hf 
import url_storage as storage
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Йоу, я бот, ееееее")

@router.message(lambda message: 'tiktok.com' in message.text or 'youtube.com' in message.text or 'youtu.be' in message.text or 'pin.it' in message.text or 'pinterest.com' in message.text or 'instagram.com' )
async def video_request(message: Message):
    url = message.text.strip()
    url_id = hf.generate_url_id(url)
    storage.url_storage[url_id] = url
    storage.save_urls(storage.url_storage)
    storage.url_storage = storage.load_urls()
    await message.answer("Ну що, такие каким кощерным способом будем скачивать", reply_markup= await in_kb.format_btn(url_id))
 