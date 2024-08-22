import telebot

bot = telebot.TeleBot(token='7111629705:AAEVuyVps_oRAwM_ghmgaIQchpcOKQB6it8')


def get_ideal_weight(height, weight):
    weight = float(weight)
    height = float(height)
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return 'худой'
    elif 18.5 < bmi <= 25:
        return 'нормальный'
    elif 25 < bmi <= 29.9:
        return 'Избыточный вес'
    return None


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/start':
        bot.send_message(
            message.from_user.id,
            'Привет, напиши свое имя, свой возраст, свой рост, свой вес, свой пол. '
            'Например: Arsen, возраст = 22, рост = 1.84, вес = 65, пол = мужской или женсий'
        )

    elif message.text != '':
        name, age, height, weight, gender = message.text.split(',')
        res = get_ideal_weight(weight=weight, height=height)
        bot.send_message(message.from_user.id, text=res)


bot.polling(none_stop=True, interval=0)


