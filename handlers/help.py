from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


router = Router()

help_keyboard = InlineKeyboardBuilder(
    [
        [InlineKeyboardButton(text="Проверить IMEI", callback_data="check_imei")],
    ]
)


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Я могу выполнять следующие команды",
        reply_markup=help_keyboard.as_markup(),
    )
