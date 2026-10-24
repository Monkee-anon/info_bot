from aiogram import Router, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    CallbackQuery,
    Message,
    InlineKeyboardButton
)
from handlers.routes import theory_keyboard

router = Router()

def task_keyboard_rus():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Окончания глаголов (11 задание)", callback_data="11_zad_rus"))
    builder.add(InlineKeyboardButton(text="Слитное/раздельное написание слов с НЕ (13 задание)", callback_data="13_zad_rus"))
    builder.add(InlineKeyboardButton(text="Слитное/раздельное написание (14 задание)", callback_data="14_zad_rus"))
    builder.add(InlineKeyboardButton(text="Н/НН в причастиях (15 задание)", callback_data="15_zad_rus"))
    builder.add(InlineKeyboardButton(text="Запятые (16 задание)", callback_data="16_zad_rus"))
    builder.add(InlineKeyboardButton(text="Запятые (18 задание)", callback_data="18_zad_rus"))
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="back_to_choice:rus"))
    return builder.as_markup()

def task_keyboard_math():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Вероятность (шаблоны)", callback_data="vero"))
    builder.add(InlineKeyboardButton(text="8 задание", callback_data="8_zad_math"))
    builder.add(InlineKeyboardButton(text="Производная (9 задание)", callback_data="9_zad_math"))
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="back_to_choice:math"))
    return builder.as_markup()

@router.callback_query(F.data.startswith ("back_to_choice:"))
async def back_to_choice_proc(call: CallbackQuery):
    await call.answer()

    subject = call.data.split(":")[1]
    # subject_name = "Русский язык" if call.data == "rus" else "Математика"

    await call.message.edit_text(text="я не помню что тут писать",
                                 reply_markup=theory_keyboard(subject))