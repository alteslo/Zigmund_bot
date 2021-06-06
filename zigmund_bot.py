from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types
import logging
import random

TOKEN = '1770518581:AAFQkOjj-BmbfxxaudziF7g_rNBwNVuiEZU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


'''
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
'''


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
