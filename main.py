import telebot
from config import API_TELEGRAM_TOKEN, chat_id

bot = telebot.TeleBot(token=API_TELEGRAM_TOKEN)


@bot.message_handler(content_types=['text'])
def repeat_message(message):  # Функция для обработки сообщений
    bot.send_message(message.chat.id, message.text)  # Отправка ответа


bot.polling()
