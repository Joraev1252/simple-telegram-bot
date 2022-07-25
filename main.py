import telebot
from bot_telegram import *

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(content_types=['text'])
# def message_handler(message):
    # if message.text == 'Qalesan Robi':
    #     bot.send_message(message.chat.id, 'Assalomu aleykum Azamjonaka')
    #     bot.send_message(message.chat.id, 'tuzumisiz nam gapla')
    #
    # elif message.text == 'yahshi rahmat Hudoga shukur':
    #     bot.send_message(message.chat.id, 'bitta gap etimi')
    #     bot.send_message(message.chat.id, 'faqat tori chunin')
    #
    # elif message.text == 'nma gap tinchlimi':
    #     bot.send_message(message.chat.id, 'man sizzi qattu sevaman')
    #     bot.send_message(message.chat.id, 'tori chunin ichimdini ettim')
    #
    # if message.text == 'manam':
    #     bot.send_message(message.chat.id, '❤️')

    # else:
    #     bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['text'])
def message_handler(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(True)