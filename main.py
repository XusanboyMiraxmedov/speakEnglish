import logging
from oxfordLookup import getDefinitions
from googletrans import Translator
translator = Translator()

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5695662829:AAELLjMHTZVna5GjeXNz6DzQEowhOLjP4CQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):



    await message.reply("Salom botimizga hush kelibsiz")



@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if lang == 'en':
        word_id = message.text
    else:
        word_id = translator.translate(message.text, dest='en').text
    if len(message.text.split()) <= 2:
        lookup = getDefinitions(word_id)
    if lookup == False:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        await message.reply(f"Word: {word_id}\n"
                            f"Definitions:\n{lookup['definitions']}")
        if lookup.get('audio'):
            await message.reply_voice(lookup['audio'])



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)