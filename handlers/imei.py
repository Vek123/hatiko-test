import pprint

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.imei import IMEIStates
from services.imei import IMEICheckService
from settings import settings


router = Router()


@router.callback_query(F.data == "check_imei")
async def handle_imei(call: CallbackQuery, state: FSMContext):
    await state.set_state(IMEIStates.imei)
    await call.message.answer("Введите IMEI:")


@router.message(IMEIStates.imei)
async def check_imei(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Проверяю Ваш IMEI...")
    if len(message.text) != 15:
        await message.answer("IMEI должен быть длинной 15. Попробуйте ещё раз.")
    elif not message.text.isdigit():
        await message.answer("IMEI должен состоять только из цифр. Попробуйте ещё раз.")
    with IMEICheckService(settings.api_live_token, message.text) as service:
        result = await service.check_imei()
        if not result:
            result = "Что-то пошло не так. Попробуйте ещё раз."
        pp = pprint.PrettyPrinter(indent=4)
        await message.answer(pp.pformat(result))
