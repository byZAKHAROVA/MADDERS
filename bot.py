import telebot
from telebot import types


TOKEN = '5404702941:AAHF2i6QaMZsxFB-1s7T0voXpRkH9XrotGs'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item1 = types.KeyboardButton('Как заказать товар?')
    item2 = types.KeyboardButton('Каталог')
    item3 = types.KeyboardButton('✰Индивидуальный заказ!✰')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)


    mess = f'Привет, {message.from_user.first_name}! Я помогу тебе оставаться стильными даже в условиях санкций! Только оригинал по самой низкой цене на рынке❗️'
    bot.send_message(message.chat.id, mess, reply_markup=markup)

#получить в чате всю инфу по пользователю bot.send_message(message.chat.id, message)
@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет!":
        bot.send_message(message.chat.id, "И тебе привет! Готов стать стильным?")
    elif message.text == "id":
        bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}')
    elif message.text == "info":
        bot.send_message(message.chat.id, message)
    elif message.text == "Как заказать товар?":
        avito_url = 'https://www.avito.ru/user/3bdbced608963f05f2732f2b5eb97ef8/profile?src=sharing'
        bot.send_message(message.chat.id, "Окэээй, лэтс гоу!")
        bot.send_message(message.chat.id, f"1) Через наш Авито: {avito_url}\n 2) Просматриваете каталог, нажимаете оформить заказ.\n - С вами свяжется наш менеджер, чтобы уточнить размер и адрес доставки.\n - оформляем доставку по вашему адресу.\n - оплачиваете - посылка уже едет к вам! \n 3)Индивидуальный заказ!\n")
    elif message.text == "Каталог":
        text = '@madders_shop_bot'
        bot.send_message(message.chat.id, "Окэээй, лэтс гоу! Скорее залетай и выбирай шмотки!")
        bot.send_message(message.chat.id, text)
    elif message.text == "✰Индивидуальный заказ!✰":
        special_order(message)
    elif message.text == "Получить доступ к боту!":
        get_acess(message)
    elif message.text == "Назад":
        start(message)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю:(")


@bot.message_handler()
def special_order(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item4 = types.KeyboardButton('Получить доступ к боту!')
    item5 = types.KeyboardButton('Назад')
    markup.add(item4)
    markup.add(item5)
    manager = '@pollythecreator'
    bot.send_message(message.chat.id,
                     f"//Индивидуальный заказ\nЭто платная услуга. Всего за ! 500 рублей ! вы сможете: \n1) иметь доступ к платному боту \n2) заказывать абсолютно ЛЮБЫЕ товары с ранков Китая, Италии и Турции по самым низким ценам! \n3) не париться с доставкой! Мы возьмем на себя разговоры с поставщиками, прохождение таможки и оформление доставки! \nОплата производится переводом нашему менеджеру {manager}")
    bot.send_message(message.chat.id,
                     f"//Как это работает?\n 1) Присылаете боту название и размер вещи, которую хотите приобрести.\n 2) Бот уточняет информацию по заказу и передает её поставщикам. \n 3) Менеджер сообщит вам точную цену и расчетную дату получения.\n 4)Оплачиваете переводом- посылка уже едет к вам!(при личной встрече в Москве оплата после получения товара)\nс уважением, MADDERS.", reply_markup=markup)




def get_acess(message):
    manager = '@pollythecreator'
    pay_num = '+79107061833'
    bot.send_message(message.chat.id,
                         f"//Почти всё готово!Осталось оплатить доступ!\nЦена: 500 руб.\nНомер для оплаты: {pay_num}\nПосле перевода, пришлите менеджеру ({manager}) квитанцию для получения ссылки на бота!\nВперед за покупками!♡")


bot.polling(none_stop=True)
