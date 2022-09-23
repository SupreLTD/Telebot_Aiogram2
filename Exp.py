from aiogram import Bot, Dispatcher, types
from aiogram import executor

bot = Bot(token='')
dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = 'I am Bot'
    get_me = await bot.get_me()
    print(get_me)

    send_message = await bot.send_message(chat_id=chat_id, text=f'{get_me.id}')
    # print(send_message.to_python())
    # send_photo = await bot.send_photo(chat_id=chat_id,
    #                      photo='https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png')
    # print(send_photo.photo[-1].file_unique_id)
    # result = await bot.set_chat_title(chat_id=5696216420,title='Learning_Bot_by_Kastus')
    # print(result)
    # invite_link = await bot.export_chat_invite_link(chat_id=5696216420)
    # print(invite_link)


executor.start_polling(dp)