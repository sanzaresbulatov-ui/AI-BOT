import telebot
from config import TOKEN
import requests
from config import API_KEY
from urllib.parse import quote
from pathlib import Path
from main import create_img

bot = telebot.TeleBot(TOKEN)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ИИ Бот, способный по твоему соообщению сгенерировать картинку")

@bot.message_handler(content_types=['text'])
def get_message(message):
    text = message.text
    bot.send_message(message.chat.id, "Генерирую картинку...")
    filename = create_img(text)

    
    with open(filename, "rb") as photo:
        bot.send_photo(
            message.chat.id,
            photo,
            caption=f"Твой запрос: {text}"
        )
#else:
    #bot.send_message(message.chat.id, "Не удалось создать картинку")


bot.polling(none_stop=True)
