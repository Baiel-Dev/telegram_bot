import telebot
from telebot import types
bot = telebot.TeleBot(token='7305120100:AAHlr6jMhtO5nHdiVH7-4M-ug90IJ3K6VjE')








@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/Hello':
        bot.send_message(
            message.from_user.id,
            'Привет, сейчас мы узнаем про твою телосложенте'
        )



class Bim:
    def __init__(self):
        a = input('имя: ')
        c = int(input('возраст: '))
        d = float(input("рост ведите в метрах: "))
        i = int(input('вес: '))
        self.name = a
        self.age = c
        self.рост =  d
        self.вес = i


    def bm(self):
        return self.вес/ self.рост ** 2

    def check(self):
        bmi = self.bm()
        if bmi <= 18.5:
            print('худой')
        elif 18.5 < bmi <= 25:
            print('нормално')
        elif 25 < bmi <= 29.9:
            print('Избыточный вес')

        else:
            print('Ожирение')

    def info(self):
        print('#' * 10)
        print('BMI')
        print(f'Name:  {self.name}')
        print(f'age: {self.age}')
        print(f'height: {self.рост}')
        print(f'weight: {self.вес}')




bot.polling(none_stop=True, interval=0)


ob = Bim()
ob.info()
ob.check()



