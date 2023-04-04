from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных
    port: str  # port


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


# Создаем экземпляр класса Env
env: Env = Env()

# Добавляем в переменные окружения данные, прочитанные из файла .env
env.read_env()

# Создаем экземпляр класса Config и наполняем его данными из переменных окружения
config = Config(tg_bot=TgBot(token=env('token')),
                db=DatabaseConfig(database=env('db_name'),
                                  db_host=env('host'),
                                  db_user=env('user'),
                                  db_password=env('password'),
                                  port=env('port')))