import telebot
import os
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID =361767303  #8447605623:AAHpc0NBpEn2rCIc03TlKwUbubaM10reeaw

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,
        "Анонимный канал обратной связи.\n\n"
        "Напишите сообщение одним текстом.\n"
        "Имя отправителя не передаётся."
    )

@bot.message_handler(content_types=["text"])
def handle(message):
    admin_text = (
        "📩 Анонимный отзыв\n"
        f"{datetime.now().strftime('%d.%m %H:%M')}\n\n"
        f"{message.text}"
    )
    bot.send_message(ADMIN_CHAT_ID, admin_text)
    bot.send_message(message.chat.id, "Принято.")

bot.infinity_polling()
