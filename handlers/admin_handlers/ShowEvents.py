from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types, Router
from aiogram import Dispatcher
from create_bot import dp, bot
from aiogram.fsm.context import FSMContext
from source.admin_states import AdminState
from keyboards.reply_keyboards import AdminMainMenu, UserMainMenu
from keyboards.inline_keyboards import InlineRegMenu
from sql_methods import sql_admins, sql_sublists, sql_qq, sql_events
from aiogram.filters import Command, StateFilter, Text


router: Router = Router()

slovar = {
    'AdminState:admin' : 1,
    'AdminState:user' : 404
}


@router.message(Command(commands = 'events'), StateFilter(AdminState.admin, AdminState.user))
async def ShowEventsProcess(message : types.Message, state : FSMContext):
    isAdmin = slovar[await state.get_state()]
    EventArray = await sql_events.extract_events()
    if EventArray == 404:
        if isAdmin == 1:
            await message.answer('Нет актуальных мероприятий', reply_markup = AdminMainMenu)
    else:
        for i in range (0, len(EventArray)):
            #ФОРМИРОВАНИЕ ТЕКСТА СООБЩЕНИЯ
            EventId = EventArray[i][0]
            EventName = EventArray[i][1]
            EventDescription = EventArray[i][2]
            day = str(EventArray[i][3]).split('-')[2]
            CorrectDay = day.split(' ')[0]
            month = str(EventArray[i][3]).split('-')[1]
            year = str(EventArray[i][3]).split('-')[0]
            time = str(EventArray[i][3]).split(' ')[1]
            EventDate = (f'{CorrectDay}.{month}.{year} {time}')
            EventPhotoId = EventArray[i][4]
            URL = EventArray[i][5]
            EventType = EventArray[i][6]
            #ФОРМИРОВАНИЕ КЛАВИАТУРЫ
            IsSub = await sql_sublists.try_sub(EventId, message.from_user.id)
            Menu = await InlineRegMenu(isAdmin, URL, EventId, IsSub, message.from_user.id)
            if EventPhotoId != 0:
                await bot.send_photo(message.from_user.id, EventPhotoId, caption=f"""{EventName}
{EventType} мероприятие
{EventDescription}
дата проведения: {EventDate}""", reply_markup = Menu)
            else:
                await message.answer(f"""{EventName}
{EventType} мероприятие
{EventDescription}
дата проведения: {EventDate}""", reply_markup = Menu)
    await message.answer(f'{len(EventArray)} мероприятий', reply_markup = AdminMainMenu)


@router.message(Text(startswith = 'EVENTdelete_'), StateFilter(AdminState.admin))
async def DeleteEventCallback(callback : types.CallbackQuery):
    EventName = callback.data.split('_')[1]
    await sql_events.delete_event(EventName)
    await callback.message.delete()
