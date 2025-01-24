from aiogram.fsm.state import StatesGroup, State


class IMEIStates(StatesGroup):
    imei = State()
