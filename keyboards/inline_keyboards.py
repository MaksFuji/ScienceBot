from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BackButton = InlineKeyboardButton(text = "ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ", callback_data= "go_back")

TiosButton_1 = InlineKeyboardButton(text = "ИНФОРМАЦИЯ", callback_data= "tios_button_info")
TiosButton_2 = InlineKeyboardButton(text = "ДОСТИЖЕНИЯ", callback_data= "tios_button_achievments")
TiosButton_3 = InlineKeyboardButton(text = "КОНТАКТЫ", callback_data= "tios_button_contacts")
TiosMenu =  InlineKeyboardMarkup(row_width=1)
TiosMenu.insert(TiosButton_1).insert(TiosButton_2).insert(TiosButton_3).insert(BackButton)

BisButton_1 = InlineKeyboardButton(text = "ИНФОРМАЦИЯ", callback_data= "bis_button_info")
BisButton_2 = InlineKeyboardButton(text = "ДОСТИЖЕНИЯ", callback_data= "bis_button_achievments")
BisButton_3 = InlineKeyboardButton(text = "КОНТАКТЫ", callback_data= "bis_button_contacts")
BisMenu =  InlineKeyboardMarkup(row_width=1)
BisMenu.insert(BisButton_1).insert(BisButton_2).insert(BisButton_3).insert(BackButton)

SubButton_1 = InlineKeyboardButton(text = "ПОДПИСАТЬСЯ НА ВСЕ НОВОСТИ", callback_data = "sub_button_all")
SubButton_2 = InlineKeyboardButton(text = "ПОДПИСАТЬСЯ НА ВНУТРЕННИЕ НОВОСТИ", callback_data = "sub_button_inside")
SubButton_3 = InlineKeyboardButton(text = "ПОДПИСАТЬСЯ НА СТОРОННИЕ НОВОСТИ", callback_data = "sub_button_outside")
SubButton_4 = InlineKeyboardButton(text = "ОТПИСАТЬСЯ ОТ ВСЕХ НОВОСТЕЙ", callback_data = "sub_button_unsub")
SubMenu = InlineKeyboardMarkup(row_width = 1)
AdminSubMenu = InlineKeyboardMarkup(row_width=1)
AdminSubMenu.insert(SubButton_1).insert(SubButton_2).insert(SubButton_3).insert(SubButton_4).insert(BackButton)
SubMenu.insert(SubButton_3).insert(SubButton_4).insert(BackButton)

async def CreateAcessMenu(log, isAdmin, isTarget):
    AcessMenu = InlineKeyboardMarkup(row_width=1)
    if isTarget != '0':
        Tdata = f'promotion_{log}_{isTarget}'
        PromotionButton = InlineKeyboardButton(text = "ПОВЫСИТЬ", callback_data= Tdata)
        AcessMenu.insert(PromotionButton)
    if isAdmin == 404 and isTarget == '0':
        Adata = f'make_admin_{log}'
        HighAcessButton = InlineKeyboardButton(text = "СДЕЛАТЬ АДМИНИСТРАТОРОМ", callback_data= Adata)
        AcessMenu.insert(HighAcessButton)
    Ddata = f'USERdelete_{log}_{isTarget}'
    DeleteButton = InlineKeyboardButton(text = "УДАЛИТЬ", callback_data= Ddata)
    AcessMenu.insert(DeleteButton)
    return AcessMenu

async def InlineRegMenu(isAdmin, isURL, id_, login_flag, log):
    RegMenu = InlineKeyboardMarkup(row_width=1)
    if isAdmin != 404:
        DeleteData = f'EVENTdelete_{id_}'
        DeleteButton = InlineKeyboardButton(text="УДАЛИТЬ МЕРОПРИЯТИЕ", callback_data=DeleteData)
        RegMenu.insert(DeleteButton)
    if login_flag == 1 and isURL == '0':
        UnSubData = f'unsub_event_{id_}_{log}'
        UnSubButton = InlineKeyboardButton(text="ОТПИСАТЬСЯ", callback_data=UnSubData)
        RegMenu.insert(UnSubButton)
        return RegMenu
    if login_flag == 404 and isURL == '0':
        SubData = f'sub_event_{id_}_{log}'
        SubButton = InlineKeyboardButton(text="ПОДПИСАТЬСЯ", callback_data=SubData)
        RegMenu.insert(SubButton)
        return RegMenu
    if isURL != '0':
        UrlButton = InlineKeyboardButton(text="ПРИНЯТЬ УЧАСТИЕ", url=isURL)
        RegMenu.insert(UrlButton)
        return RegMenu

async def InlineFormMenu(id_): #ПЕРЕНЕСТИ В СЕРВИСНУЮ ПАПКУ
	BackButton = InlineKeyboardButton(text = "ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ", callback_data= "go_back")
	data = f'create_form_{id_}'
	CreateFormButton = InlineKeyboardButton(text = "СОЗДАТЬ ФОРМУ", callback_data= data)
	EventFormMenu = InlineKeyboardMarkup(row_width=1)
	EventFormMenu.insert(CreateFormButton).insert(BackButton)
	return EventFormMenu