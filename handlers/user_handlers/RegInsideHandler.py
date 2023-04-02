from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types, Router, F
from aiogram import Dispatcher
from create_bot import dp, bot
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from keyboards.reply_keyboards import  UserMainMenu, RoleMenu, AspirantMenu
from sql_methods import sql_admins, sql_users
from source import admin_states
from aiogram.filters import Command, StateFilter, Text
from source.admin_states import AdminState

router: Router = Router()

slovar = {
    'Соискатель' : 'aspirant',
    'Разработчик' : 'razrab',
    'Дизайнер' : 'designer',
    'СММщик' : 'smm',
    'Организатор' : 'org'
}

class InsideSteps(StatesGroup):
    Type = State()
    Aspirant = State()
    Add = State()


@router.message(Command(commands='reg'))
async def WelcomeInsideProcess(message : types.Message, state : FSMContext):
    await message.answer(f'Привет, {message.from_user.full_name}, выбери свою должность', reply_markup = RoleMenu)
    await state.set_state(InsideSteps.Type)


@router.message(StateFilter(InsideSteps.Type))
async def TypeProcess(message : types.Message, state : FSMContext):
    try:
        await state.update_data(type = slovar[message.text])
    except:
        await message.answer(f'{message.from_user.full_name}, выбери свою должность <u>на клавиатуре!</u>', reply_markup = RoleMenu)
        return
    if slovar[message.text] == 'aspirant':
        await message.answer(f'{message.text} {message.from_user.full_name}, пожалуйста выбери свою будущую профессию', reply_markup = AspirantMenu)
        await state.set_state(InsideSteps.Aspirant)
    else:
        await message.answer(f'Отлично, {message.text}, отправь мне своё <u>ФИО и фотографию</u> одним сообщением!', reply_markup = types.ReplyKeyboardRemove())
        await state.set_state(InsideSteps.Add)


@router.message(StateFilter(InsideSteps.Aspirant))
async def AspirantProcess(message : types.Message, state : FSMContext):
    try:
        if slovar[message.text] == 'aspirant':
            await message.answer(f'{message.from_user.full_name} <u>ТЫ УЖЕ СОИСКАТЕЛЬ</u>, попробуй еще раз', reply_markup = AspirantMenu)
            return
        await state.update_data(target = slovar[message.text])
    except:
        await message.answer(f'{message.from_user.full_name}, выбери свою должность <u>на клавиатуре!</u>', reply_markup = AspirantMenu)
        return
    await message.answer(f'Отлично, {message.text}, отправь мне своё <u>ФИО и фотографию</u> одним сообщением!', reply_markup = types.ReplyKeyboardRemove())
    await state.set_state(InsideSteps.Add)


@router.message(F.photo, StateFilter(InsideSteps.Add)) # проверить фильтр фото
async def AddInsideProcess(message : types.Message, state : FSMContext):
    if message.caption is None:
        await message.answer(f'Попробуй еще раз, {message.from_user.full_name}')
    else:
        data = await state.get_data()
        try:
            res = await sql_users.add_user(message.from_user.id, message.caption, data['type'], data['target'], message.photo[0].file_id)
        except:
            res = await sql_users.add_user(message.from_user.id, message.caption, data['type'], 0, message.photo[0].file_id)
        if res == 606:
            await message.answer(f'{message.from_user.full_name} ты уже зарегистрирован!', reply_markup = UserMainMenu)
            await state.set_state(AdminState.user)
        else:
            name = (message.caption).split(',')[0]
            await message.answer(f'Поздравляем, {message.from_user.full_name}, ты успешно зарегистрирован под именем {name}', reply_markup = UserMainMenu)
            await state.set_state(AdminState.user)

