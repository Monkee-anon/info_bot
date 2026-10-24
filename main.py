from os import getenv
import asyncio
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from handlers.routes import router
from aiogram.types import BotCommand
from aiohttp import web
import os

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)

dp = Dispatcher()

dp.include_router(router)

async def handle(request):
    return web.Response(text="Бот успешно работает!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Веб-сервер запущен на порту {port}")

async def main():
    asyncio.create_task(start_web_server())

    commands = [
        BotCommand(command="start", description="Запустить бота"),
        #BotCommand(command="help", description="Запустить бота")
    ]

    await bot.set_my_commands(commands=commands)

    print("start")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())