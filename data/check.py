from aiogram.fsm.state import StatesGroup, State

class AddPhoto(StatesGroup):
    name = State()
    photo = State()