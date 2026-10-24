from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    CallbackQuery,
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

router = Router()

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='/about')],
            [KeyboardButton(text='Start'), KeyboardButton(text='Help')],
        ],
        resize_keyboard=True,
    )
    return keyboard

def get_main_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Open Site', url='https://youtu.be/dQw4w9WgXcQ?si=Aiiz1ym-jZJ0169p')],
            [InlineKeyboardButton(text='More', callback_data='more_info')],
        ]
    )
    return keyboard

@router.callback_query(lambda c: c.data == 'more_info')
async def more_info(callback: CallbackQuery):
    await callback.message.answer('More info')
    await callback.answer()

@router.message(Command('start'))
@router.message(F.text.lower() == 'start')
async def start(message: Message):
    await message.answer('*Hello!* I\'m right _behind_ you, don\'t turn\n\n'
                         'Type /help for help, but no one can help you anyway',
                         parse_mode='Markdown')

@router.message(Command('help'))
async def heelp(message: Message):
    await message.answer('Commands:\n<i>/start</i> - starts a bot\n<i>/help</i> - list of commands\n<i>/about</i> - about us',
                         parse_mode='HTML',
                         reply_markup=get_main_reply_keyboard())

@router.message(Command('about'))
async def about(message: Message):
    await message.answer(f'About bot. Your name is {message.from_user.first_name}', reply_markup=get_main_inline_keyboard())

@router.message()
async def text(message: Message):
    await message.answer('pasword chmo')