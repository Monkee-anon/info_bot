import json
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    CallbackQuery,
    Message,
    InputMediaPhoto
    )
from handlers.keyboards import (inline_keyboard,
                                theory_keyboard,
                                task_keyboard_rus,
                                task_keyboard_math,
                                veroyatnost_keyboard,
                                inf_theory_keyboard,
                                practice_or_theory_keyboard,
                                choice_theory_keyboard,
                                choice_practice_keyboard,
                                zadachi_5_list_keyboard,
                                inf_practice_keyboard,
                                get_task_keyboard,
                                get_veroyatnost_keyboard,
                                zadachi_5_keyboard,
                                inf_navigation_keyboard,
                                temporary_back_keyboard
                                )

router = Router()


@router.callback_query(F.data.in_({"rus", "math"}))
async def theory(call: CallbackQuery):
    await call.answer()
    subject_code = call.data
    subject_name = "Русский язык" if call.data == "rus" else "Математика"
    await call.message.edit_text(
        text=f"Вы выбрали предмет {subject_name}",
        reply_markup=theory_keyboard(subject=subject_code)
    )

@router.callback_query(F.data == "inf")
async def inf_proc(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text="Вы выбрали предмет Информатика",
                                 reply_markup=practice_or_theory_keyboard())

@router.callback_query(F.data == "choice_theory")
async def choice_theory(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text="Вы выбрали предмет Информатика",
                                 reply_markup=choice_theory_keyboard())

@router.callback_query(F.data == "watch_theory_inf")
async def watch_theory_inf(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text="Выберите тему",
                                 reply_markup=inf_theory_keyboard())


@router.callback_query(F.data.startswith("watch_th:"))
async def watch_theory(call: CallbackQuery):
    await call.answer()

    action, subject = call.data.split(":")

    if subject == "rus":
        await call.message.edit_text("Выберите задание",
                                     reply_markup=task_keyboard_rus())
    elif subject == "math":
        await call.message.edit_text("Выберите задание",
                                     reply_markup=task_keyboard_math())


@router.callback_query(F.data.startswith("add_th:"))
async def add_theory(call: CallbackQuery):
    await call.answer()

    action, subject = call.data.split(":")

    if subject == "rus":
        await call.message.edit_text("К сожалению, данная функция пока недоступна",
                                     reply_markup=temporary_back_keyboard(subject=subject))
    elif subject == "math":
        await call.message.edit_text("К сожалению, данная функция пока недоступна",
                                     reply_markup=temporary_back_keyboard(subject=subject))
    elif subject == "inf":
        await call.message.edit_text("К сожалению, данная функция пока недоступна",
                                     reply_markup=temporary_back_keyboard(subject=subject))

@router.callback_query(F.data == "back_subjects")
async def back_subjects(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(f"Привет, {call.from_user.first_name}!\nПожалуйста, выберите предмет",
                         reply_markup=inline_keyboard())

@router.callback_query(F.data.startswith ("back_to_choice:"))
async def back_to_choice_proc(call: CallbackQuery):
    await call.answer()

    subject = call.data.split(":")[1]
    subject_name = "Русский язык" if subject == "rus" else "Математика"


    await call.message.edit_text(text=f"Вы выбрали предмет {subject_name}",
                                 reply_markup=theory_keyboard(subject=subject))

@router.callback_query(F.data.contains("zad"))
async def show_task_theory(call: CallbackQuery):
    await call.answer()

    callback_data= call.data
    parts = callback_data.split("_")
    task_num = parts[0]
    subject = parts[2]

    key = f"{task_num}_{subject}"

    with open("data/photos.json", "r", encoding="utf-8") as f:
        photos = json.load(f)

    photo_list = photos.get(key, [])

    if not photo_list:
        if subject == "rus":
            keyboard = task_keyboard_rus()
        else:
            keyboard = task_keyboard_math()
        await call.message.answer("К сожалению, теории по этому заданию пока нет",
                                  reply_markup=keyboard)
    else:
        current_task = int(task_num)
        media_group = [InputMediaPhoto(media=photo_id) for photo_id in photo_list]
        await call.message.answer_media_group(media=media_group)
        await call.message.answer("Навигация по заданиям:",
                                  reply_markup=get_task_keyboard(current_num=current_task, subject=subject))

@router.callback_query(F.data.startswith("back_to_list_"))
async def back_to_tasks_list(call: CallbackQuery):
    await call.answer()
    subject = call.data.split("_")[-1]

    await call.message.delete()

    if subject == "rus":
        keyboard = task_keyboard_rus()
    elif subject == "math":
        keyboard = task_keyboard_math()
    await call.message.answer("Выберите задание",
                              reply_markup=keyboard)


@router.callback_query(F.data == "vero")
async def vero_proc(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text="Выберите шаблон",
                                 reply_markup=veroyatnost_keyboard())

@router.callback_query(F.data.startswith("pattern"))
async def veroyatnost_show(call: CallbackQuery):
    await call.answer()

    callback_data= call.data
    parts = callback_data.split("_")
    task_num = parts[1]
    key = f"ver_pat{task_num}"
    # print(task_num)

    with open("data/photos.json", "r", encoding="utf-8") as f:
        photos = json.load(f)

    photo_list = photos.get(key, [])

    if not photo_list:
        await call.message.answer("К сожалению, теории по этому заданию пока нет")
    else:
        current_num = int(task_num)
        media_group = [InputMediaPhoto(media=photo_id) for photo_id in photo_list]
        await call.message.answer_media_group(media=media_group)
        await call.message.answer("Навигация",
                                  reply_markup=get_veroyatnost_keyboard(current_num=current_num))


@router.callback_query(F.data == "back_to_choice_inf")
async def back_to_choice_inf(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text="Вы выбрали предмет Информатика",
                                 reply_markup=practice_or_theory_keyboard())

@router.callback_query(F.data == "choice_practice")
async def choice_practice(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text="Вы выбрали предмет Информатика",
                                 reply_markup=choice_practice_keyboard())

@router.callback_query(F.data == "probs_list")                              #список заданий для практики по информатике
async def zadachi_list(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text="Выберите задание",
                                 reply_markup=inf_practice_keyboard())

@router.callback_query(F.data == "5_num_inf")                               #список задач номер 5 по информатике
async def fifth_zad_inf(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text="Выберите задание",
                                 reply_markup=zadachi_5_list_keyboard())

@router.callback_query(F.data.startswith("inf_5_"))                         #выбрать действие: посмотреть задачу/решение
async def inf_5_proc(call: CallbackQuery):
    await call.answer()

    callback_data = call.data
    parts = callback_data.split("_")
    task_num_str = parts[-1]
    task_num = int(task_num_str)
    await call.message.edit_text("Выберите действие",
                                 reply_markup=zadachi_5_keyboard(task_num=task_num))

@router.callback_query(F.data.startswith("show_"))
async def inf_5(call: CallbackQuery):
    await call.answer()

    callback_data = call.data
    parts = callback_data.split("_")
    task_num_str = parts[-1]
    action = parts[1]
    task_num = int(task_num_str)
    key = f"5_{task_num}_{action}"
    # print(task_num_str, key)

    with open("data/photos.json", "r", encoding="utf-8") as f:
        photos = json.load(f)

    photo_list = photos.get(key, [])

    media_group = [InputMediaPhoto(media=photo_id) for photo_id in photo_list]
    await call.message.answer_media_group(media=media_group)
    await call.message.answer(f"Задача номер {task_num}. Выберите действие",
                              reply_markup=inf_navigation_keyboard(task_num=task_num, action=action))


@router.callback_query(F.data.startswith("bits_etc"))
async def perevod_show(call: CallbackQuery):
    await call.answer()

    with open("data/photos.json", "r", encoding="utf-8") as f:
        photos = json.load(f)

    key = "inf_perevod"
    photo_list = photos.get(key, [])

    media_group = [InputMediaPhoto(media=photo_id) for photo_id in photo_list]
    await call.message.answer_media_group(media=media_group)
    await call.message.answer("Выберите тему",
                              reply_markup=inf_theory_keyboard())

@router.callback_query(F.data == "7_formulas")
async def formulas_show(call: CallbackQuery):
    await call.answer()

    with open("data/photos.json", "r", encoding="utf-8") as f:
        photos = json.load(f)

    key = "7_formulas"
    photo_list = photos.get(key, [])

    media_group = [InputMediaPhoto(media=photo_id) for photo_id in photo_list]
    await call.message.answer_media_group(media=media_group)
    await call.message.answer("Выберите тему",
                              reply_markup=inf_theory_keyboard())

@router.callback_query(F.data == "add_problem")
async def add_problem(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text("К сожалению, данная функция пока недоступна",
                                     reply_markup=temporary_back_keyboard(subject="inf"))


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\nПожалуйста, выберите предмет",
                         reply_markup=inline_keyboard())