from aiogram.filters import BaseFilter
from aiogram.types import Message
import re


class FilterDate(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if isinstance(message.text, str):
            self.str_date: list = ['date']
            self.str_date = re.findall(r"(\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}:\d{1,2})", message.text)
            return message.text in self.str_date
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
