from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

router = Router()

def inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Русский язык", callback_data="rus"))
    builder.add(InlineKeyboardButton(text="Информатика", callback_data="inf"))
    builder.add(InlineKeyboardButton(text="Математика", callback_data="math"))
    builder.adjust(2)
    return builder.as_markup()


def theory_keyboard(subject: str):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Посмотреть теорию", callback_data=f"watch_th:{subject}"))
    builder.add(InlineKeyboardButton(text="Добавить теорию", callback_data=f"add_th:{subject}"))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="Вернуться к выбору предметов", callback_data="back_subjects"))
    return builder.as_markup()


def task_keyboard_rus():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Окончания глаголов (11 задание)", callback_data="11_zad_rus"))
    builder.add(InlineKeyboardButton(text="Слитно/раздельно с НЕ (13 задание)", callback_data="13_zad_rus"))
    builder.add(InlineKeyboardButton(text="Слитно/раздельно (14 задание)", callback_data="14_zad_rus"))
    builder.add(InlineKeyboardButton(text="Н/НН в причастиях (15 задание)", callback_data="15_zad_rus"))
    builder.add(InlineKeyboardButton(text="Запятые (16 задание)", callback_data="16_zad_rus"))
    builder.add(InlineKeyboardButton(text="Запятые (18 задание)", callback_data="18_zad_rus"))
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="back_to_choice:rus"))
    return builder.as_markup()


def task_keyboard_math():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Вероятность (шаблоны)", callback_data="vero"))
    builder.add(InlineKeyboardButton(text="6 задание", callback_data="6_zad_math"))
    builder.add(InlineKeyboardButton(text="8 задание", callback_data="8_zad_math"))
    builder.add(InlineKeyboardButton(text="Производная (9 задание)", callback_data="9_zad_math"))
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="back_to_choice:math"))
    return builder.as_markup()

def veroyatnost_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Объяснение всех типов", callback_data="pattern_0"))
    builder.add(InlineKeyboardButton(text="Шаблон 1. Кофейные автоматы ", callback_data="pattern_1"))
    builder.add(InlineKeyboardButton(text="Шаблон 2. ПЦР-тесты", callback_data="pattern_2"))
    builder.add(InlineKeyboardButton(text="Шаблон 3. Стрелок и патроны (до первого попадания)", callback_data="pattern_3"))
    builder.add(InlineKeyboardButton(text="Шаблон 4. Монеты", callback_data="pattern_4"))
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="back_to_choice:math"))
    return builder.as_markup()

def practice_or_theory_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Теория", callback_data=f"choice_theory"))
    builder.add(InlineKeyboardButton(text="Практика", callback_data="choice_practice"))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="Вернуться к выбору предметов", callback_data="back_subjects"))
    return builder.as_markup()

def choice_practice_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Список заданий", callback_data="probs_list"))
    builder.add(InlineKeyboardButton(text="Добавить задание", callback_data="add_problem"))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="back_to_choice_inf"))
    return builder.as_markup()

def zadachi_5_list_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Задача 1", callback_data="inf_5_1"))
    builder.add(InlineKeyboardButton(text="Задача 2", callback_data="inf_5_2"))
    builder.add(InlineKeyboardButton(text="Задача 3", callback_data="inf_5_3"))
    builder.add(InlineKeyboardButton(text="Задача 4", callback_data="inf_5_4"))
    builder.add(InlineKeyboardButton(text="Задача 5", callback_data="inf_5_5"))
    builder.add(InlineKeyboardButton(text="Задача 6", callback_data="inf_5_6"))
    builder.add(InlineKeyboardButton(text="Задача 7", callback_data="inf_5_7"))
    builder.add(InlineKeyboardButton(text="Задача 8", callback_data="inf_5_8"))
    builder.add(InlineKeyboardButton(text="Задача 9", callback_data="inf_5_9"))
    builder.add(InlineKeyboardButton(text="Задача 10", callback_data="inf_5_10"))
    builder.add(InlineKeyboardButton(text="Задача 11", callback_data="inf_5_11"))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="probs_list"))
    return builder.as_markup()

def zadachi_5_keyboard(task_num: int):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Посмотреть задание", callback_data=f"show_problem_{task_num}"))
    builder.add(InlineKeyboardButton(text="Посмотреть решение", callback_data=f"show_ans_{task_num}"))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="5_num_inf"))
    return builder.as_markup()

def inf_navigation_keyboard(task_num: int, action: str):                                                                # клавиатура для навигации по заданиям практики (высылается с фото)
    builder = InlineKeyboardBuilder()
    prev_num = task_num - 1
    next_num = task_num + 1
    if prev_num > 0:
        builder.add(InlineKeyboardButton(text=f"⬅️ {prev_num}", callback_data=f"inf_5_{prev_num}"))
    if next_num < 12:
        builder.add(InlineKeyboardButton(text=f"{next_num} ➡️", callback_data=f"inf_5_{next_num}"))
    builder.adjust(2)
    if action == "problem":
        builder.row(InlineKeyboardButton(text="Показать решение", callback_data=f"show_ans_{task_num}"))
    builder.row(InlineKeyboardButton(text="К списку задач", callback_data="5_num_inf"))
    return builder.as_markup()

def choice_theory_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Посмотреть теорию", callback_data="watch_theory_inf"))
    builder.add(InlineKeyboardButton(text="Добавить теорию", callback_data="add_th:inf"))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="back_to_choice_inf"))
    return builder.as_markup()

def inf_theory_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Перевод единиц", callback_data="bits_etc"))
    builder.add(InlineKeyboardButton(text="Формулы для 7 задания", callback_data="7_formulas"))
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="choice_theory"))
    return builder.as_markup()

def inf_practice_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="5 задание", callback_data="5_num_inf"))
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="back_to_choice_inf"))
    return builder.as_markup()

def get_task_keyboard(current_num: int, subject: str):
    builder = InlineKeyboardBuilder()
    prev_num = current_num - 1
    next_num = current_num + 1

    if prev_num > 10:
        builder.add(InlineKeyboardButton(text=f"⬅️ {prev_num}", callback_data=f"{prev_num}_zad_{subject}"))

    builder.add(InlineKeyboardButton(text=f"{next_num} ➡️", callback_data=f"{next_num}_zad_{subject}"))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="К списку заданий", callback_data=f"back_to_list_{subject}"))
    return builder.as_markup()

def get_veroyatnost_keyboard(current_num: int):
    builder = InlineKeyboardBuilder()
    prev_num = current_num - 1
    next_num = current_num + 1

    if prev_num >= 0:
        builder.add(InlineKeyboardButton(text=f"⬅️ {prev_num} шаблон", callback_data=f"pattern_{prev_num}"))

    if next_num < 5:
        builder.add(InlineKeyboardButton(text=f"{next_num} шаблон ➡️", callback_data=f"pattern_{next_num}"))

    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="К списку шаблонов", callback_data=f"vero"))
    return builder.as_markup()

def temporary_back_keyboard(subject: str):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Назад", callback_data=subject))
    return builder.as_markup()