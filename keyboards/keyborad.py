from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

b1: KeyboardButton = KeyboardButton(text='Команда1')
b2: KeyboardButton = KeyboardButton(text='Команда2')
b4: KeyboardButton = KeyboardButton(text='Команда3')
b5: KeyboardButton = KeyboardButton(text='Команда4')

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
kb_builder.row(b2, b5).add(b1)
kb = kb_builder.as_markup(resize_keyboard=True)

kb2_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
kb2_builder.add(b1).add(b4)
kb2 = kb2_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


kb3_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
kb3_builder.add(b2).row(b1, b4, b5)
kb3 = kb3_builder.as_markup(resize_keyboard=False, one_time_keyboard=True)


inline_button_1: InlineKeyboardButton = InlineKeyboardButton(text = "Инлайн кнопка 1", callback_data= "inline_command_1")
inline_button_2: InlineKeyboardButton = InlineKeyboardButton(text = "Инлайн кнопка 2", url = 'https://vk.com/bonch.science')
inline_button_3: InlineKeyboardButton = InlineKeyboardButton(text = "Инлайн кнопка 3", callback_data= "inline_command_3")
inline_button_4: InlineKeyboardButton = InlineKeyboardButton(text = "Инлайн кнопка 4", callback_data= "inline_command_4")

InlineMenu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
InlineMenu_builder.add(inline_button_1).add(inline_button_2).add(inline_button_3).add(inline_button_4)
InlineMenu = InlineMenu_builder.as_markup(row_width=1)


