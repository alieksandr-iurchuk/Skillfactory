import telebot
from config import exchanger, TOKEN
from extensions import APIExteption, Converter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Что бы начать работу введите команду боту в следующем формате:\n<имя валюты, цену на которую нужно узнать> \
<имя валюты, цену в которой нужно узнать> \
<количество переводимой валюты>\nУвидить список всех доступных валют: /values'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    text += "\n".join(f"{i+1}) {key}" for i, key in enumerate(exchanger.keys()))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
        values = message.text.split()
        values = list(map(str.lower, values))
        # if len(values) != 3:
        #     raise ValueError('Неверное количество параметров!')
        # val1, val2, amount = values
        try:
            total_base = Converter.get_price(values)
        except APIExteption as e:
            bot.reply_to(message, f'Ошибка пользователя.\n{e}')
        except Exception as e:
            bot.reply_to(message, f'Не удалось обработать команду\n{e}')
        else:
            text = f'Цена {values[0]} в {values[1]} {values[2]} - {total_base} {exchanger[values[1]]}'
            bot.send_message(message.chat.id, text)


bot.polling(none_stop=True, interval=0)