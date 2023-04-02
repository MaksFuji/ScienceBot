from aiogram import Bot, types
from aiogram import Dispatcher
import os
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import config

storage = MemoryStorage()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(storage=storage)
