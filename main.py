import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import logging

from config import TOKEN, WEBHOOK_URL
from handlers import register_handlers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
register_handlers(dp)

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    await bot.set_my_commands([
        BotCommand(command="/start", description="شروع"),
        BotCommand(command="/help", description="راهنما"),
    ])
    logging.info("ربات راه‌اندازی شد و Webhook تنظیم شد.")

async def on_shutdown(app):
    await bot.delete_webhook()
    logging.info("ربات خاموش شد.")

def main():
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook")
    setup_application(app, dp, bot=bot)
    web.run_app(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()