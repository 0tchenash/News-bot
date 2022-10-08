from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import inline_keyboard

from config import TOKEN


News_bot = Bot(token=TOKEN)
dp = Dispatcher(News_bot)

async def on_startup(_):
    print('bot is online!')

@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply(text="Hello! I'm simply telegram-bot! I collect news! \n How can I help?\n ",
                        reply_markup=inline_keyboard.HELP)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await News_bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)