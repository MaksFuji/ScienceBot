from aiogram import types, Router
from aiogram import Dispatcher
from aiogram.filters import Command, CommandStart, StateFilter, Text
from keyboards.reply_keyboards import AdminMainMenu, UserMainMenu, MenuNotsNil, AdministrationMenu
from keyboards.inline_keyboards import TiosMenu, SubMenu, AdminSubMenu, BisMenu
from sql_methods import sql_admins
from source import admin_states
from source.admin_states import AdminState
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

import lexicon

router: Router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def WelcomeProcess(message: types.Message, state: FSMContext):
    # global AdminResult
    AdminResult = await sql_admins.log_in(message.from_user.id)
    if AdminResult == 1:
        await state.set_state(AdminState.admin)
        await message.delete()
        await message.answer(text=f"{message.from_user.full_name}, {lexicon.LEXICON_ADMIN_RU['/start']}",
                             reply_markup=AdminMainMenu)
    else:
        await state.set_state(AdminState.user)
        await message.delete()
        await message.answer(text=f"{message.from_user.full_name}, {lexicon.LEXICON_USER_RU['/start']}",
                             reply_markup=UserMainMenu)


@router.message(Command(commands='НОЦЫ_НИЛЫ'), StateFilter(AdminState.user))
async def NotsNilProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['nil_info'], reply_markup=MenuNotsNil)


@router.message(Command(commands='НОЦЫ_НИЛЫ'), StateFilter(AdminState.admin))
async def AdminNotsNilProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['nil_info'], reply_markup=MenuNotsNil)


@router.message(Command(commands='Контакты'), StateFilter(AdminState.user))
async def ContactsProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['contacts_info'], reply_markup=UserMainMenu)


@router.message(Command(commands='Контакты'), StateFilter(AdminState.admin))
async def AdminContactsProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['contacts_info'], reply_markup=AdminMainMenu)


@router.message(Command(commands='О_комитете'), StateFilter(AdminState.user))
async def AboutProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['about_us'], reply_markup=UserMainMenu)


@router.message(Command(commands='О_комитете'), StateFilter(AdminState.admin))
async def AdminAboutProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['about_us'], reply_markup=AdminMainMenu)


@router.message(Command(commands='Подписки'), StateFilter(AdminState.user))
async def SubsProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['destroy_keyboards'], reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text=lexicon.LEXICON_USER_RU['subs_main'], reply_markup=SubMenu)


@router.message(Command(commands='Подписки'), StateFilter(AdminState.admin))
async def AdminSubsProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['destroy_keyboards'], reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text=lexicon.LEXICON_USER_RU['subs_main'], reply_markup=AdminSubMenu)


@router.message(Command(commands='ТИОС'), StateFilter(AdminState.user))
async def TiosProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['destroy_keyboards'], reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text=lexicon.LEXICON_USER_RU['tios_main'], reply_markup=TiosMenu)


@router.message(Command(commands='БИС'), StateFilter(AdminState.user))
async def BisProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['destroy_keyboards'], reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text=lexicon.LEXICON_USER_RU['bis_main'], reply_markup=BisMenu)


@router.message(Command(commands='ТИОС'), StateFilter(AdminState.admin))
async def AdminTiosProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['destroy_keyboards'], reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text=lexicon.LEXICON_USER_RU['tios_main'], reply_markup=TiosMenu)


@router.message(Command(commands='БИС'), StateFilter(AdminState.admin))
async def AdminBisProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['destroy_keyboards'], reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text=lexicon.LEXICON_USER_RU['bis_main'], reply_markup=BisMenu)

@router.message(Command(commands='Прочее'), StateFilter(AdminState.admin))
async def AdminBisProcess(message: types.Message):
    await message.delete()
    await message.answer(text=lexicon.LEXICON_USER_RU['nots_nil_other'])


@router.message(Command(commands='Администрация'))
async def AdministrationProcess(message: types.Message, state: FSMContext):
    AdminResult = await sql_admins.log_in(message.from_user.id)
    if AdminResult == 1:
        await message.delete()
        await message.answer(text=lexicon.LEXICON_USER_RU['destroy_keyboards'],
                             reply_markup=types.ReplyKeyboardRemove())
        await message.answer(text=lexicon.LEXICON_ADMIN_RU['list_admin'], reply_markup=AdministrationMenu)
        await state.set_state(AdminState.admin)
        # отправлять список админимстрации с фотками
    else:
        await message.answer(text=f"{message.from_user.full_name}, {lexicon.LEXICON_USER_RU['not_admin']}",
                             reply_markup=UserMainMenu)


@router.callback_query(Text(startswith='go_back'), StateFilter(AdminState.user))
async def UserBackCallback(callback: types.CallbackQuery):
    await callback.message.answer(text=lexicon.LEXICON_USER_RU['back_main_menu'], reply_markup=UserMainMenu)


@router.callback_query(Text(text='go_back'), StateFilter(AdminState.admin))
async def AdminBackCallback(callback: types.CallbackQuery):
    await callback.message.answer(text=lexicon.LEXICON_USER_RU['back_main_menu'], reply_markup=AdminMainMenu)


@router.callback_query(Text(startswith='tios_button_'))
async def TiosCallback(callback: types.CallbackQuery):
    print(callback)
    result = callback.data.split('_')[2]
    if result == "info":
        await callback.message.answer(text=lexicon.LEXICON_USER_RU['tios_info'])
    elif result == "achievments":
        await callback.message.answer(text=lexicon.LEXICON_USER_RU['tios_achiv'])
    elif result == "contacts":
        await callback.message.answer(text=lexicon.LEXICON_USER_RU['tios_contacts'])


@router.callback_query(Text(startswith="bis_button_"))
async def BisCallback(callback: types.CallbackQuery):
    result = callback.data.split('_')[2]
    if result == "info":
        await callback.message.answer(text=lexicon.LEXICON_USER_RU['bis_info'])
    elif result == "achievments":
        await callback.message.answer(text=lexicon.LEXICON_USER_RU['bis_achiv'])
    elif result == "contacts":
        await callback.message.answer(text=lexicon.LEXICON_USER_RU['bis_contacts'])


@router.callback_query(Text(text="administration_button_"), StateFilter(AdminState.admin))
async def AdministrationCallback(callback: types.CallbackQuery):
    result = callback.data.split('_')[2]
    if result == 'addEvent':
        # добавление меро
        await callback.message.answer(text=lexicon.LEXICON_USER_RU['add_event'])
    elif result == 'deleteEvent':
        # удаление меро
        await callback.message.answer(text=lexicon.LEXICON_USER_RU['delete_event'])
    elif result == 'invite':
        # создание инвайт кода
        await callback.message.answer(text=lexicon.LEXICON_USER_RU['create_invite_code'])
