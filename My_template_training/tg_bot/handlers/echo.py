from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode


async def bot_echo(message: types.Message):
    text = [
        'Эхо без состояния.',
        "Сообщение:",
        str(message.text)
    ]
    await message.answer('\n'.join(text))  # try use *text '\n'.join(text)


async def bot_all_echo(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        f'Эхо в состоянии {hcode(state_name)}.',  # hcode - machine code format
        "Сообщение:",
        message.text
    ]
    await message.answer('\n'.join(text))

def register_echo(dp: Dispatcher):

    dp.register_message_handler(bot_echo,state=None)
    dp.register_message_handler(bot_all_echo,state='*',content_types=types.ContentType.ANY)


