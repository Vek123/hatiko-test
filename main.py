import asyncio
import logging

from aiogram import Bot, Router, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from settings import settings
from handlers import router as handlers_router
from middleware import WhiteListMiddleware


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

default_router = Router()
START_MESSAGE = ("Здравствуй, %(name)s. "
                 "Я могу проверять Ваш IMEI и получать о нём информацию. "
                 "Чтобы ознакомиться с командами напишите /help")


@default_router.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(START_MESSAGE % {"name": message.from_user.full_name})


async def main():
    bot = Bot(token=settings.tg_bot_token)
    dp = Dispatcher()
    dp.include_router(default_router)
    dp.include_router(handlers_router)
    dp.message.middleware(WhiteListMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Bot is starting...")
    try:
        asyncio.run(main())
    except (RuntimeError, KeyboardInterrupt):
        logger.info("Bot is closing...")
