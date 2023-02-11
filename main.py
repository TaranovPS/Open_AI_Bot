import aiogram
import openai
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os


bot = aiogram.Bot(token=os.getenv('BOT_AI'))
dp = Dispatcher(bot)
openai.api_key = os.getenv('AI_TOKEN')


@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply("Привет! Я бот, который может отвечать на ваши вопросы с помощью OpenAI API. Попробуйте задать мне вопрос!")


@dp.message_handler()
async def answer_question(message: Message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'{message.text}',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    await bot.send_message(message.from_user.id, response.choices[0].text)


if __name__ == '__main__':
    executor.start_polling(dp)



