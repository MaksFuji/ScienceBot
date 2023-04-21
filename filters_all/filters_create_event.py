from aiogram.filters import BaseFilter
from aiogram.types import Message
import re
from datetime import datetime

# ^     Начало строки

# (     День - может писаться как 01, 1, 31
#   0?[1-9]     Необязательный ноль и чило от 1 до 9
#   |           Или
#   [12][0-9]   [1 или 2] и число [от 1 до 9]
#   |           Или
#   3[01]       30 или 31
# )

# ([./\\])    "." или "/" или "\" для разделения дня и месяца

# (     Месяц - может писаться как 01, 1, 12
#   0?[1-9]     Необязательный ноль и чило [от 1 до 9]
#   |           Или
#   1[012]      10 или 11 или 12
# )

# \2    Повторяет ([./\\]), "." или "/" или "\" для разделения месяца и года

# Год - может писаться как 2023 или 23
# (\d{2}|\d{4}) 2 или 4 числа

# [\s-] Пробел или "-" для разделения даты и времени

# Время, может быть в формате 01:01, 1:1, 23:59, 23
# (     Часы
#   [01]?[0-9]  Необязательные [0 или 1] и чило [от 0 до 9]
#   |           Или
#   2[0-3]      20, 21, 22, 23
# )
# (     Минуты (вводить не обязательно)
#   :[0-5]?[0-9]    Необязательное число [от 0 до 5] и чило [от 0 до 9]
# )?

# $     Конец строки

regex_str = r"^(0?[1-9]|[12][0-9]|3[01])([./\\])(0?[1-9]|1[012])\2(\d{2}|\d{4})[\s-]([01]?[0-9]|2[0-3])(:[0-5]?\d)?$"

class FilterDate(BaseFilter):
    """Фильтр для проверки введённой даты"""
    async def __call__(self, message: Message) -> bool:
        if isinstance(message.text, str):
            if not re.match(regex_str, message.text):
                return False

            # Выбираем день, месяц и год
            nums = [int(i) for i in re.findall(r"\d{4}|\d{3}|\d{2}|\d{1}", message.text)]
            day, month, year = nums[:3]

            if year < 100: # если год указан 2 числами, например 23, а не 2023
                year += 2000

            try:
                date = datetime(year=year, month=month, day=day)
            except ValueError: # Если введена дата, которой не существует, например 30 февраля
                return False

            return date > datetime.now()
        else:
            return False


class FilterWeb(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if isinstance(message.text, str):
            regex_message = re.compile('(https?://[\S]+)')
            compliance_object = regex_message.search(message.text)
            if compliance_object == None:
                self.str_web = ['web']
            else:
                self.str_web = message.text[compliance_object.start():compliance_object.end()]
            return message.text in self.str_web
        else:
            return False
