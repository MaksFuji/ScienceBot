from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


BackReplyButton: KeyboardButton = KeyboardButton(text='/Назад')


RB1: KeyboardButton = KeyboardButton(text='Соискатель')
RB2: KeyboardButton = KeyboardButton(text='Разработчик')
RB3: KeyboardButton = KeyboardButton(text='Дизайнер')
RB4: KeyboardButton = KeyboardButton(text='Организатор')
RB5: KeyboardButton = KeyboardButton(text='СММщик')

AspirantMenu_bulder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
AspirantMenu_bulder.row(RB2, RB3).row(RB4, RB5).add(BackReplyButton)
AspirantMenu = AspirantMenu_bulder.as_markup(resize_keyboard = True)

RoleMenu_bulder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
RoleMenu_bulder.add(RB1).row(RB2, RB3).row(RB4, RB5).add(BackReplyButton)
RoleMenu = RoleMenu_bulder.as_markup(resize_keyboard = True)


FormList = ['имя', 'описание', 'фото', 'дата рождения', 'факультет', 'группа', 'курс', 'Номер телефона']


#FB - FormButton
CompleteButton: KeyboardButton = KeyboardButton(text='Завершить')
FB1: KeyboardButton = KeyboardButton(text='Имя')
FB2: KeyboardButton = KeyboardButton(text='Описание')
FB3: KeyboardButton = KeyboardButton(text='Фото')
FB4: KeyboardButton = KeyboardButton(text='Дата рождения')
FB5: KeyboardButton = KeyboardButton(text='Факультет')
FB6: KeyboardButton = KeyboardButton(text='Группа')
FB7: KeyboardButton = KeyboardButton(text='Курс')
FB8: KeyboardButton = KeyboardButton(text='Номер телефона')

FormColumnMenu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
FormColumnMenu_builder.row(FB1,FB2).row(FB3,FB4,FB5).row(FB6,FB7, FB8).add(CompleteButton).add(BackReplyButton)
FormColumnMenu = FormColumnMenu_builder.as_markup(resize_keyboard = True)


FormNameList = ['ФИО капитана команды', 'ФИО участника команды']
FNL1: KeyboardButton = KeyboardButton(text='ФИО капитана команды')
FNL2: KeyboardButton = KeyboardButton(text='ФИО участника команды')

FormNameColumnMenu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
FormNameColumnMenu_builder.row(FNL1).row(FNL2)
FormNameColumnMenu = FormNameColumnMenu_builder.as_markup(resize_keyboard = True)


MainButton_1: KeyboardButton = KeyboardButton(text='/НОЦЫ_НИЛЫ')
MainButton_2: KeyboardButton = KeyboardButton(text='/Контакты')
MainButton_3: KeyboardButton = KeyboardButton(text='/О_комитете')
MainButton_4: KeyboardButton = KeyboardButton(text='/Подписки')
MainButton_5: KeyboardButton = KeyboardButton(text='/Администрация')

AdminMainMenu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
AdminMainMenu_builder.row(MainButton_1, MainButton_2, MainButton_3).row(MainButton_4, MainButton_5)
AdminMainMenu = AdminMainMenu_builder.as_markup(resize_keyboard=True)

UserMainMenu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
UserMainMenu_builder.row(MainButton_1, MainButton_2, MainButton_3).row(MainButton_4)
UserMainMenu = UserMainMenu_builder.as_markup(resize_keyboard=True)


NotsNilButton_1: KeyboardButton = KeyboardButton(text='/ТИОС')
NotsNilButton_2: KeyboardButton = KeyboardButton(text='/БИС')
NotsNilButton_3: KeyboardButton = KeyboardButton(text='/Прочее')

MenuNotsNil_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
MenuNotsNil_builder.row(NotsNilButton_1, NotsNilButton_2, NotsNilButton_3).row(BackReplyButton)
MenuNotsNil = MenuNotsNil_builder.as_markup(resize_keyboard=True)


AdministrationButton_1: KeyboardButton = KeyboardButton(text='/Добавить_мероприятие')
#AdministrationButton_2 = KeyboardButton('/Удалить_мероприятие')
AdministrationButton_2: KeyboardButton = KeyboardButton(text='/Управление_персоналом')

AdministrationMenu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
AdministrationMenu_builder.row(AdministrationButton_1, AdministrationButton_2).row(BackReplyButton)
AdministrationMenu = AdministrationMenu_builder.as_markup(resize_keyboard=True)

EventTypeButton_1: KeyboardButton = KeyboardButton(text='Внутреннее')
EventTypeButton_2: KeyboardButton = KeyboardButton(text='Внешнее')

EventTypeMenu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
EventTypeMenu_builder.row(EventTypeButton_1, EventTypeButton_2, BackReplyButton)
EventTypeMenu = EventTypeMenu_builder.as_markup(resize_keyboard=True)
