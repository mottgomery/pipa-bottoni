import asyncio
import os

from aiogram import Bot, Dispatcher, types


from handlers import commands, callback

BOT_TOKEN='8409827058:AAHIQ2W66s1rhKDKLHe6vDssm_ZPtRN6Xyk'

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    try:
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        dp.include_router(commands.router)
        dp.include_router(callback.router)
        print("Bot started")
        await dp.start_polling(bot)
        await bot.session.close()
    except Exception as ex:
        print(f'Error: {ex}')
    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
