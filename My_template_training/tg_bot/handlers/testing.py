from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from My_template_training.tg_bot.misc.states import Test


async def testing(message: types.Message):
    await message.answer('Вы начали тестирование\n'
                         'Вопрос №1.\n\n'
                         'Вы робот?')
    await Test.Q1.set()
    # await Test.first()


async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # await state.update_data(answer1=answer) #через update
    # await state.update_data( # через словарь
    # {'answer1':answer}
    # )
    async with state.proxy() as data:  # Через генератор
        data['answer1'] = answer

    await message.answer('Вопрос №2.\n'
                         'Ваша память ухудшилась?')

    # await Test.Q2.set()
    await Test.next()

async def answer_2(message:types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text

    await message.answer('Спасибо за Ваши ответы')
    await message.answer(f'Ответ 1: {answer1}')
    await message.answer(f'Ответ 2: {answer2}')

    await state.finish() # сброс состояний
    await state.reset_state() # так же сбрасывает состояние
    await state.reset_state(with_data=False) # Сбрасывает состояние, но сохраняет данные


def register_testing(dp: Dispatcher):
    dp.register_message_handler(testing, Command('test'))
    dp.register_message_handler(answer_q1, state=Test.Q1)
    dp.register_message_handler(answer_2, state=Test.Q2)