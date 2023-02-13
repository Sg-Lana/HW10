import telebot
from telebot import types
bot = telebot.TeleBot("6177152313:AAFvR7txdHjrScwDO-5slmk7fLp49KB7Ypo")

@bot.message_handler(commands=["start"])
def calc(message):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание клавиатуры
    but1 = types.KeyboardButton("Рациональные") 
    but2 = types.KeyboardButton("Комплексные")
    mrk.add(but1)
    mrk.add(but2)
    bot.send_message(message.chat.id, f"калькулятор \nсделайте выбор, с какими числами будете работать",reply_markup=mrk)

@bot.message_handler(content_types=['text'])
def buttons(message):
    global typeNums
    a = types.ReplyKeyboardRemove()
    if message.text == "Рациональные":
        bot.send_message(message.chat.id, f'Выбран режим рациональных чисел', reply_markup=a)
        bot.send_message(message.chat.id, f'введите выражнение разделяя пробелами')
        bot.register_next_step_handler(message, controller)
        typeNums = 0
    elif message.text == "Комплексные":
        bot.send_message(message.chat.id, f'Выбран режим комплексных чисел', reply_markup=a)
        bot.send_message(message.chat.id, f'введите выражнение разделяя пробелами')
        bot.register_next_step_handler(message, controller)
        typeNums = 1

def controller(message):
    global res
    global znak
    line = message.text.split()
    znak = line[1]
    if typeNums == 0:
        a = int(line[0])
        b = int(line[2])
    else:
        a = complex(line[0])
        b = complex(line[2])

    if znak == '+':
        res = summ_nums(a, b)
    elif znak == '-':
        res = sub_nums(a, b)
    elif znak == '*':
        res = mult_nums(a, b)
    elif znak == '/':
        res = div_nums(a, b)
    elif typeNums == 1 and (znak == '//' or znak == '%'):
        bot.send_message(message.chat.id, f'Неверный ввод, повторите')
        bot.register_next_step_handler(message, controller)
        #return
    elif znak == '//':
        res = div_int(a, b)
    elif znak == '%':
        res = div_rem(a, b)
    bot.send_message(message.chat.id, {res})  

    def summ_nums(a, b):
        return (a + b)

    def sub_nums(a, b):
        return (a - b)

    def mult_nums(a, b):
        return (a * b)

    def div_nums(a, b):
        return a / b

    def div_int(a, b):
        return (a // b)

    def div_rem(a, b):
        return (a % b)

bot.infinity_polling()





