import telebot
from config import API_TELEGRAM_TOKEN, chat_id

bot = telebot.TeleBot(token=API_TELEGRAM_TOKEN)


def filter_text(message):
    text = ["привет", "пока"]
    return message.text.lower() in text


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        chat_id=message.from_user.id,
        text=f"Привет, {message.from_user.first_name}! Я бот-визитка.\n\n"
             f"<i>Ознакомиться с функционалом можно использовав</i> - <b>/help</b>",
        parse_mode="html"
    )


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(
        chat_id=message.from_user.id,
        text=f"<b><u>Я умею:</u></b>\n\n"
             f"<b>/start</b> - выводит приветственное сообщение\n"
             f"<b>/help</b> - выводит, что я умею\n"
             f"<b>/about</b> - выводит личную информацию\n\n"
             f"<b>На сообщения <code>привет</code>/<code>пока</code> я буду здороваться/прощаться</b>\n"
             f"<b>На любые другие сообщения я буду писать, <i>Вы напечатали: (то что ты написал)</i></b>",
        parse_mode="html"
    )


@bot.message_handler(commands=['about'])
def start_message(message):
    bot.send_message(
        chat_id=message.from_user.id,
        text=f"Привет, {message.from_user.first_name}!\nМеня зовут Тихон, мне 15 лет.\n"
             f"Я учусь в 10 классе и на курсе нейросетей от "
             f"<a href='https://practicum.yandex.ru/'><b>Яндекс Практикума</b></a>\n"
             f"Умею писать Telegram ботов, также люблю работать в фотошопе\n",
        parse_mode="html",
        disable_web_page_preview=True
    )


@bot.message_handler(content_types=['text'])
def hi_message(message):  # Функция для обработки сообщений
    bot.send_message(
        chat_id=message.from_user.id,
        text=f"Извини, но я не понял, что ты написал(\n<i>Используй <b>/help</b>, чтобы узнать доступные команды</i>",
        parse_mode="html"
    )


bot.polling()
