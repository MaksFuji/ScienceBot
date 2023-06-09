from aiogram import types, Router
from aiogram import Dispatcher
from create_bot import dp, bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from keyboards.reply_keyboards import  UserMainMenu, AdminMainMenu
from keyboards.inline_keyboards import  CreateAcessMenu
from sql_methods import sql_admins, sql_users
from source import admin_states
from source.admin_states import AdminState
from aiogram.types import message
from aiogram.filters import Command, CommandStart, StateFilter, Text


router: Router = Router()


slovar = {
    404 : 'Сотрудник комитета',
    1 : 'Администратор ресурса',
    'aspirant1' : 'Поздравляем, ты прошел собеседование!',
    'aspirant0' : 'Кажется, ты не прошел собеседование(',
    'aspirant': 'Соискатель',
    'razrab': 'Разработчик',
    'designer': 'Дизайнер',
    'smm': 'СММщик',
    'org':'Организатор'

}


@router.message(Command(commands='Управление_персоналом'), StateFilter(AdminState.admin))
async def ShowProcess(message : types.Message, state : FSMContext):
    UserList = await sql_users.show_users()
    UID = message.from_user.id
    if UserList == 404:
        await message.answer('NO INSIDE SUBS', reply_markup = AdminMainMenu)
        await state.set_state(AdminState.admin)
    else:
        for i in range(0, len(UserList)):
            isAdmin = await sql_admins.log_in(UserList[i][1])
            target = await sql_users.extract_target(UserList[i][1])
            menu = await CreateAcessMenu(UserList[i][1], isAdmin, target)
            try:
                t = f', желаемая должность: {slovar[UserList[i][5]]}'
            except:
                t = ''
            await bot.send_photo(UID, UserList[i][3], caption=f'{slovar[isAdmin]} {UserList[i][2]}, {slovar[UserList[i][4]]} {t}',
                                 reply_markup=menu)
        await bot.send_message(UID, f'{len(UserList)} - количество авторизованных пользователей', reply_markup = AdminMainMenu)


@router.callback_query(Text(startswith='make_admin_'), StateFilter(AdminState.admin))
async def AcessCallback(callback : types.CallbackQuery, state: FSMContext):
    log = callback.data.split('_')[2]
    result = await sql_admins.add_admin(log)
    if result == 606:
        await callback.answer('пользователь уже существует', show_alert = True)
        await state.set_state(AdminState.admin)
    else:
        await callback.answer(f'{callback.from_user.full_name}, вы зарегистрировали нового администратора', show_alert = True)
        await bot.send_message(log, f'Ты стал администратором!!!', reply_markup = AdminMainMenu)
        await state.set_state(AdminState.admin)


@router.callback_query(Text(startswith="USERdelete_"), StateFilter(AdminState.admin))
async def DeleteCallback(callback : types.CallbackQuery, state: FSMContext):
    log = callback.data.split('_')[1]
    AspirantAnswer = callback.data.split('_')[2]
    if AspirantAnswer == '0':
        await sql_users.delete_user(log)
        await sql_admins.delete_admin(log)
        await callback.message.delete()
        await bot.send_message(log, 'Ты исключен из отдела', reply_markup = UserMainMenu)
    else:
        AspirantAnswer = f'{AspirantAnswer}0'
        await bot.send_message(log, f'{slovar[AspirantAnswer]}', reply_markup = UserMainMenu)
    await state.set_state(AdminState.admin)


@router.callback_query(Text(startswith="promotion_"), StateFilter(AdminState.admin))
async def PromotionCallback(callback : types.CallbackQuery, state: FSMContext):
    log = callback.data.split('_')[1]
    target = callback.data.split('_')[2]
    result = await sql_users.promotion(log, target)
    if result == 404:
        await callback.message.answer('Такого пользователя не существует!', reply_markup = AdminMainMenu)
    elif result == 606:
        await callback.message.answer('Человека некуда повышать!', reply_markup = AdminMainMenu)
    elif result == 1:
        await callback.answer(f'{callback.from_user.full_name}, ты повысил человека!', show_alert = True)
        await bot.send_message(log, f'Ты повышен до {slovar[target]}а', reply_markup = UserMainMenu)
    await state.set_state(AdminState.admin)

