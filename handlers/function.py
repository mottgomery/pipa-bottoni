import hashlib
import os
import yt_dlp
import time 
from aiogram.types import FSInputFile


def generate_url_id(url: str):
    return hashlib.md5(url.encode()).hexdigest()

async def download_video_and_send(bot, chat_id, url, media_type):
    yt_opts = {
        'format': 'best[ext=mp4]' if media_type == 'video' else 'bestaudio[ext=m4a]/best',
        'outtmpl': f"downloads/%(title)s.{'mp4' if media_type == 'video' else 'm4a'}",

    }

    try:
        start_time = time.time()
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        end_time = time.time()
        elapsed_time = end_time - start_time

        media_file = FSInputFile(file_path)
        if media_type == 'video':
            await bot.send_video(chat_id, media_file, caption=f"ну загрузка заняла {elapsed_time:.2f} кошерных мнгновений, хз зачем знать это, но надо, на видева")
        else:
            await bot.send_audio(chat_id, media_file, caption=f"ну загрузка заняла {elapsed_time:.2f} кошерных мнгновений, хз зачем знать это, но надо, на музыка")

        os.remove(file_path)
    except Exception as e:
        await bot.send_message(chat_id, f"БАБАШИБКА АААААААА: {str(e)}")
