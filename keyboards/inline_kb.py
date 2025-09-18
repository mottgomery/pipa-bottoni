from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def format_btn(url_id):
    buttons = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="видева", callback_data=f"download_video:{url_id}")],
            [InlineKeyboardButton(text="аудива", callback_data=f"download_audio:{url_id}")]
        ])
    return buttons
