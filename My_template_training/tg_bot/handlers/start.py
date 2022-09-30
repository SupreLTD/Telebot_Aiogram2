from typing import re
import re as standardre

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.deep_linking import get_start_link


async def start_bot(message: types.Message):
    args = message.get_args()
    await message.answer('You are pressed "start"')
    await message.answer(f'Тебя привел пользователь с ID: {args}')


async def start_deeplink(message: types.Message):
    deep_link = await get_start_link(payload='123')
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в тестовом боте\n'
                         f'У Вас нет диплинка \n'
                         f'Ваш диплинк - {deep_link}')


def register_user(dp: Dispatcher):
    dp.register_message_handler(start_bot, CommandStart(deep_link=standardre.compile(r'^[a-z0-9_-]{3,15}$')))
    dp.register_message_handler(start_deeplink, CommandStart())
