import asyncio
import logging
import os

from create_bot import dp, bot
# Добавление команд
from handlers.user_handlers import RegInsideHandler, ServiceHandlers, SimpleHandlers
from handlers.admin_handlers import CreateEventHandler, CreateFormHandler, AcessHandlers, ShowEvents, SubHandlers

# Инициализируем логгер
logger = logging.getLogger(__name__)


async def main():
    os.system('cls')

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')



    dp.include_router(ServiceHandlers.router)
    dp.include_router(SimpleHandlers.router)
    dp.include_router(SubHandlers.router)
    dp.include_router(CreateEventHandler.router)
    dp.include_router(CreateFormHandler.router)
    dp.include_router(RegInsideHandler.router)
    dp.include_router(AcessHandlers.router)
    dp.include_router(ShowEvents.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
