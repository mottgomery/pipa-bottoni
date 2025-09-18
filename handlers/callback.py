from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from handlers.function import download_video_and_send
import url_storage as storage


router = Router()

@router.callback_query(lambda callback: 'video' in callback.data or 'audio' in callback.data)
async def format_selection(callback: CallbackQuery, bot: Bot):
    storage.url_storage = storage.load_urls()
    action, url_id = callback.data.split(':')
    url = storage.url_storage.get(url_id)
    if not url:
        await callback.message.answer("БАБАШИБКА АААААААА: URL не найден")
        return
    await callback.message.answer(f"ДЕЛАЕМ...")
    if action == 'download_video':
        await download_video_and_send(bot, callback.message.chat.id, url, media_type="video")
    elif action == 'download_audio':
        await download_video_and_send(bot, callback.message.chat.id, url, media_type="audio")  
 
