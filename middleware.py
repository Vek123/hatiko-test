from typing import Callable, Dict, Awaitable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from settings import settings


class WhiteListMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ):
        if event.from_user.username not in settings.tg_users_whitelist:
            return event.reply("У вас нет доступа к этому боту.")
        return await handler(event, data)
