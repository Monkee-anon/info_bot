from os import getenv
import asyncio
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from handlers.routes import router
from aiogram.types import BotCommand

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

dp.include_router(router)

async def main():
    bot = Bot(token=TOKEN)

    commands = [
        BotCommand(command="start", description="Запустить бота"),
        #BotCommand(command="help", description="Запустить бота")
    ]

    await bot.set_my_commands(commands=commands)

    print("start")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())