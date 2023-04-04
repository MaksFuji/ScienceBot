from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state


class AdminState(StatesGroup):
    admin = State()
    user = State()


# тут были функции, через которые можно было получать состояния админа и юзера