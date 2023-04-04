from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

BackButton: InlineKeyboardButton = InlineKeyboardButton(text="ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ", callback_data='go_back')


TiosButton_1: InlineKeyboardButton = InlineKeyboardButton(text="ИНФОРМАЦИЯ", callback_data="tios_button_info")
TiosButton_2: InlineKeyboardButton = InlineKeyboardButton(text="ДОСТИЖЕНИЯ", callback_data="tios_button_achievments")
TiosButton_3: InlineKeyboardButton = InlineKeyboardButton(text="КОНТАКТЫ", callback_data="tios_button_contacts")
TiosMenu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
TiosMenu_builder.row(TiosButton_1, TiosButton_2, TiosButton_3, BackButton, width=1)
TiosMenu = TiosMenu_builder.as_markup()


BisButton_1: InlineKeyboardButton = InlineKeyboardButton(text="ИНФОРМАЦИЯ", callback_data="bis_button_info")
BisButton_2: InlineKeyboardButton = InlineKeyboardButton(text="ДОСТИЖЕНИЯ", callback_data="bis_button_achievments")
BisButton_3: InlineKeyboardButton = InlineKeyboardButton(text="КОНТАКТЫ", callback_data="bis_button_contacts")
BisMenu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
BisMenu_builder.row(BisButton_1, BisButton_2, BisButton_3, BackButton, width=1)
BisMenu = BisMenu_builder.as_markup()


SubButton_1: InlineKeyboardButton = InlineKeyboardButton(text="ПОДПИСАТЬСЯ НА ВСЕ НОВОСТИ", callback_data="sub_button_all")
SubButton_2: InlineKeyboardButton = InlineKeyboardButton(text="ПОДПИСАТЬСЯ НА ВНУТРЕННИЕ НОВОСТИ", callback_data="sub_button_inside")
SubButton_3: InlineKeyboardButton = InlineKeyboardButton(text="ПОДПИСАТЬСЯ НА СТОРОННИЕ НОВОСТИ", callback_data="sub_button_outside")
SubButton_4: InlineKeyboardButton = InlineKeyboardButton(text="ОТПИСАТЬСЯ ОТ ВСЕХ НОВОСТЕЙ", callback_data="sub_button_unsub")
SubMenu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
SubMenu_builder.row(SubButton_1, SubButton_2, SubButton_3, SubButton_4, BackButton, width=1)
SubMenu = SubMenu_builder.as_markup()

AdminSubMenu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
AdminSubMenu_builder.row(SubButton_3, SubButton_4, BackButton, width=1)
AdminSubMenu = AdminSubMenu_builder.as_markup()

async def CreateAcessMenu(log, isAdmin, isTarget):
    AcessMenu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    if isTarget != '0':
        Tdata = f'promotion_{log}_{isTarget}'
        PromotionButton: InlineKeyboardButton = InlineKeyboardButton(text="ПОВЫСИТЬ", callback_data=Tdata)
        AcessMenu_builder.row(PromotionButton, width=1)
        AcessMenu = AcessMenu_builder.as_markup()
    if isAdmin == 404 and isTarget == '0':
        Adata = f'make_admin_{log}'
        HighAcessButton: InlineKeyboardButton = InlineKeyboardButton(text="СДЕЛАТЬ АДМИНИСТРАТОРОМ", callback_data=Adata)
        AcessMenu_builder.row(HighAcessButton, width=1)
        AcessMenu = AcessMenu_builder.as_markup()
    Ddata = f'USERdelete_{log}_{isTarget}'
    DeleteButton: InlineKeyboardButton = InlineKeyboardButton(text="УДАЛИТЬ", callback_data=Ddata)
    AcessMenu_builder.row(DeleteButton, width=1)
    AcessMenu = AcessMenu_builder.as_markup()
    return AcessMenu


async def InlineRegMenu(isAdmin, isURL, id_, login_flag, log):
    RegMenu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    if isAdmin != 404:
        DeleteData = f'EVENTdelete_{id_}'
        DeleteButton: InlineKeyboardButton = InlineKeyboardButton(text="УДАЛИТЬ МЕРОПРИЯТИЕ", callback_data=DeleteData)
        RegMenu_builder.row(DeleteButton, width=1)
        RegMenu = RegMenu_builder.as_markup()
    if login_flag == 1 and isURL == '0':
        UnSubData = f'unsub_event_{id_}_{log}'
        UnSubButton: InlineKeyboardButton = InlineKeyboardButton(text="ОТПИСАТЬСЯ", callback_data=UnSubData)
        RegMenu_builder.row(UnSubButton, width=1)
        RegMenu = RegMenu_builder.as_markup()
        return RegMenu
    if login_flag == 404 and isURL == '0':
        SubData = f'sub_event_{id_}_{log}'
        SubButton: InlineKeyboardButton = InlineKeyboardButton(text="ПОДПИСАТЬСЯ", callback_data=SubData)
        RegMenu_builder.row(SubButton, width=1)
        RegMenu = RegMenu_builder.as_markup()
        return RegMenu
    if isURL != '0':
        UrlButton: InlineKeyboardButton = InlineKeyboardButton(text="ПРИНЯТЬ УЧАСТИЕ", url=isURL)
        RegMenu_builder.row(UrlButton, width=1)
        RegMenu = RegMenu_builder.as_markup()
        return RegMenu


async def InlineFormMenu(id_):  # ПЕРЕНЕСТИ В СЕРВИСНУЮ ПАПКУ
    BackButton: InlineKeyboardButton = InlineKeyboardButton(text="ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ", callback_data="go_back")
    data = f'create_form_{id_}'
    CreateFormButton: InlineKeyboardButton = InlineKeyboardButton(text="СОЗДАТЬ ФОРМУ", callback_data=data)
    EventFormMenu = InlineKeyboardMarkup(inline_keyboard=[[CreateFormButton],
                                                          [BackButton]]
                                         )
    return EventFormMenu
