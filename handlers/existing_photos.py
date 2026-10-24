from aiogram import Router, F
import json
from aiogram.types import Message
from aiogram.filters import Command
# from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from data.check import AddPhoto


router = Router()

file = "data/photos.json"

# class AddPhoto(StatesGroup):
#     name = State()
#     photo = State()

async def save_photo(photo_name, photo_id):
    try:
        with open(file, "r", encoding="utf-8") as f:
            photos = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        photos = {}

    if photo_name not in photos:
        photos[photo_name] = []

    if photo_id not in photos[photo_name]:
        photos[photo_name].append(photo_id)


    with open(file, 'w', encoding='utf-8') as f:
        json.dump(photos, f, ensure_ascii=False, indent=4)


# @router.message(F.photo)
# async def photo_id_cmd(message: Message):
#
#     photo = message.photo[-1]
#     photo_id = photo.file_id
#
#
#     await message.reply_photo(photo_id, caption=f"ID: {photo_id}")
#
#     photo_base = {
#         "id": photo_id
#     }
#     save_photo(photo_name, photo_id)

# @router.message(Command("start"))
# async def start(message: Message):
#     await photo_cmd(message)

@router.message(Command("add"))
async def add_photo_state(message: Message, state: FSMContext):
    await state.set_state(AddPhoto.name)
    await message.answer("Введите название задания")

@router.message(AddPhoto.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(photo_name=message.text)
    await state.set_state(AddPhoto.photo)
    await message.answer("Имя сохранено. Теперь пришлите фото")

@router.message(AddPhoto.photo, F.photo)
async def photo_cmd(message: Message, state: FSMContext):

    photo_id = message.photo[-1].file_id
    data = await state.get_data()
    photo_name = data.get("photo_name")

    await save_photo(photo_name, photo_id)
    await message.answer(f"Фото сохранено для задания {photo_name}")

@router.message(AddPhoto.photo, Command("stop"))
async def stop_cmd(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Добавление фото успешно завершено!")