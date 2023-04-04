from aiogram import types, Router
from keyboards.reply_keyboards import AdminMainMenu, UserMainMenu
from source import admin_states
# STATES
from source.admin_states import AdminState
from handlers.admin_handlers.CreateEventHandler import CreatingSteps
from handlers.admin_handlers.CreateFormHandler import FormSteps
from handlers.user_handlers.RegInsideHandler import InsideSteps
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

router: Router = Router()


@router.message(Command(commands=['Назад']), StateFilter(AdminState.user, InsideSteps))
async def UserBackProcess(message: types.Message):
    await message.answer('Возвращаемся в главное меню', reply_markup=UserMainMenu)


@router.message(Command(commands=['Назад']), StateFilter(CreatingSteps, AdminState.admin, FormSteps))
async def AdminBackProcess(message: types.Message, state: FSMContext):
    await message.answer('Возвращаемся в главное меню', reply_markup=AdminMainMenu)
    await state.set_state(AdminState.admin)
