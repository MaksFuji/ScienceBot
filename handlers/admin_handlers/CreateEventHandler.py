from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types, Router, F
from aiogram import Dispatcher
from create_bot import dp, bot
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from datetime import datetime
from keyboards.reply_keyboards import AdminMainMenu
from sql_methods import sql_events
from keyboards.reply_keyboards import AdminMainMenu, EventTypeMenu, AdministrationMenu
from keyboards import inline_keyboards
import re 
from source import admin_states
from source.admin_states import AdminState
from aiogram.filters import Command, CommandStart, StateFilter, Text, BaseFilter
from filters_all import FilterDate, FilterWeb

router: Router = Router()


class CreatingSteps(StatesGroup):
    Title = State()
    Type = State()
    Description = State()
    Date = State()
    WebSource = State()
    Photo = State()


@router.message(Command(commands='skipdm'), StateFilter(AdminState.admin))
async def SkipFunction (message : types.Message, state : FSMContext):
    # await CreatingSteps.Photo.set()
    await state.update_data(photo = 'https://awesomeworld.ru/wp-content/uploads/2017/11/kapibary_1-700x400.jpg')
    await state.update_data(title = 'Крутое мероприятие')
    await state.update_data(type = 'Гейское')
    await state.update_data(description = 'НеНочная')
    await state.update_data(date = '2023-11-20 00')
    await state.update_data(source = 0)

    data = await state.get_data()
    result = await sql_events.add_event(data['title'], data['type'], data['description'], data['date'], data['photo'], 0, data['source'])
    kb = await inline_keyboards.InlineFormMenu(result)
    if data['source'] == 0: data['source'] = 'without source'
    await bot.send_photo(message.from_user.id, data['photo'], caption=f"""
        Downloading finished!
    +title : {data['title']}
    +type : {data['type']}
    +description : {data['description']}
    +date : {data['date']}
    +web resource : {data['source']}
            """, reply_markup = kb)
    await state.set_state(AdminState.admin)


@router.message(Command(commands = 'Добавить_мероприятие'), StateFilter(AdminState.admin))
async def WelcomeProcess(message : types.Message, state: FSMContext):
    await message.answer('Welcome text, send title', reply_markup = types.ReplyKeyboardRemove())
    await state.set_state(CreatingSteps.Title)


@router.message(StateFilter(CreatingSteps.Title))
async def UploadTitle(message : types.Message, state : FSMContext):
    await state.update_data(title = message.text)
    await message.answer('Choose type', reply_markup = EventTypeMenu)
    await state.set_state(CreatingSteps.Type)


@router.message(StateFilter(CreatingSteps.Type))
async def ChooseType(message : types.Message, state : FSMContext):
    if message.text == 'Внутреннее' or message.text == 'Внешнее':
        await state.update_data(type = message.text)
        await message.answer('send description', reply_markup = types.ReplyKeyboardRemove())
        await state.set_state(CreatingSteps.Description)
    else:
        await message.reply(f'fuck you, {message.from_user.full_name}, try again', reply_markup = EventTypeMenu)
        return


@router.message(StateFilter(CreatingSteps.Description))
async def UploadDescription(message : types.Message, state : FSMContext):
    await state.update_data(description = message.text)
    await message.answer('send date')
    await state.set_state(CreatingSteps.Date)


# ОШИБКА ПРИ ДОБАВЛЕНИИ ФОТО, ЖАЛУЕТСЯ НА ЛЯМБДА ФУНКЦИЮ В ФИЛЬТРЕ
@router.message(FilterDate(), StateFilter(CreatingSteps.Date))
async def UploadDate(message : types.Message, state : FSMContext):
    # old_date = (message.text).split('/')#ЧЕЙ ТО ТАСК
    # year = old_date[2].split(' ')[0]
    # time = old_date[2].split(' ')[1]
    # new_date = "" + year + '-' + old_date[1] + '-' + old_date[0] + ' ' + time

    nums = [int(i) for i in re.findall(r"\d{4}|\d{3}|\d{2}|\d{1}", message.text)]
    
    if len(nums) == 4: # если минуты не указаны
        day, month, year, hours = nums
        minute = 0
    else:
        day, month, year, hours, minute = nums
    
    if year < 100: # если год указан 2 числами, например 23, а не 2023
        year += 2000
    
    new_date = f"{year}-{month:02d}-{day:02d} {hours:02d}:{minute:02d}:00"

    await state.update_data(date = new_date)
    await message.answer('send web resourse or "нет"')
    await state.set_state(CreatingSteps.WebSource)


@router.message(StateFilter(CreatingSteps.Date))
async def ErrDate(message : types.Message, state : FSMContext):
    await message.reply(f'fuck you, {message.from_user.full_name}, try again')
    return


@router.message(FilterWeb(), StateFilter(CreatingSteps.WebSource))
async def UploadWebSource(message : types.Message, state : FSMContext):
    await state.update_data(source = message.text)
    await message.answer('send photo or "нет"')
    await state.set_state(CreatingSteps.Photo)


@router.message(StateFilter(CreatingSteps.WebSource))
async def ErrWebSource(message : types.Message, state : FSMContext):
    if message.text == 'нет':
        await state.update_data(source = 0)
        await message.answer('send photo or "нет"')
        await state.set_state(CreatingSteps.Photo)
    else:
        await message.reply(f'fuck you, {message.from_user.full_name}, try again')
        return



# В SQL МЕТОДЕ dd_event НЕТ ОТРАБОТКИ ОШИБОК, ПОЭТОМУ В СЛУЧАЕ ЧЕГО БОТ МОЖЕТ УПАСТЬ
@router.message(~F.photo, StateFilter(CreatingSteps.Photo))
async def SaveWithoutPhoto(message : types.Message, state : FSMContext):
    data = await state.get_data()
    result = await sql_events.add_event(data['title'], data['type'], data['description'], data['date'], 0, 0, data['source'])
    kb = await inline_keyboards.InlineFormMenu(result)
    if result != 1: # ДОЛЖНА БЫТЬ ОПЕРАЦИЯ ==, НО ДЛЯ РАБОТЫ ФУНКЦИИ ИЗМНЕНЕНО НА !=. НАДО ИСПРАВИТЬ. ТО ЕСТЬ ДОБАВИТЬ ОТРАБОТКУ ОШИБОК
        if data['source'] == 0: data['source'] = 'without source'
        await message.answer(f"""
    Downloading finished!
    +title : {data['title']}
    +type : {data['type']}
    +description : {data['description']}
    +date : {data['date']}
    +web resource : {data['source']}
    -without photo
            """, reply_markup = kb)
    await state.set_state(AdminState.admin)


@router.message(F.photo, StateFilter(CreatingSteps.Photo))
async def UploadPhoto(message : types.Message, state : FSMContext):
    await state.update_data(photo = message.photo[0].file_id)
    data = await state.get_data()
    result = await sql_events.add_event(data['title'], data['type'], data['description'], data['date'], data['photo'], 0, data['source'])
    kb = await inline_keyboards.InlineFormMenu(result)
    if data['source'] == 0: data['source'] = 'without source'
    await bot.send_photo(message.from_user.id, data['photo'], caption=f"""
        Downloading finished!
    +title : {data['title']}
    +type : {data['type']}
    +description : {data['description']}
    +date : {data['date']}
    +web resource : {data['source']}
            """, reply_markup = kb)
    await state.set_state(AdminState.admin)