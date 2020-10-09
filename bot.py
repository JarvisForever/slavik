import telebot

bot = telebot.TeleBot('1005767344:AAGf-nzkeK6uKMr9vdRiJRrqwOWHdNO0XNw')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую тебя, высшая форма жизни. Я - бот Славик, который подскажет тебе расписание уроков и не только.\nКоманды, которыми ты можешь воспользоваться:\n/homework-Доманее задание;\n/event-какие-то намечающиеся события;\n/timetable-расписание уроков и аудитории, где будут проходить уроки;\n/clock-расписание звонков;\n/menu-Вернуться назад к командам;\n(Некоторые функции могут добавляться со временем, и ты можешь подказать какую ту функцию добавить, а мой создатель подумает над этим)')

@bot.message_handler(commands=['homework'])
def start_message(message):
    bot.send_message(message.chat.id, 'Данных пока нет')

@bot.message_handler(commands=['event'])
def start_message(message):
    bot.send_message(message.chat.id, 'Пока никаких событий не произошло')

@bot.message_handler(commands=['timetable'])
def start_message(message):
    bot.send_message(message.chat.id, '---Понедельник:\n1)География\n2)История\n3)География(Захист Украины)\n4)Захист Украины\n5)Геометрия\n6)Укр.лит.\n---Вторник:\n1)Гром.осв.\n2)Англ. мова\n3)Укр.мова\n4)Укр.мова\n5)Биология\n6)Физика\n7)Физ-ра\n---Среда:\n1)Гром.осв.\n2)Физика\n3)Алгебра\n4)Укр.мова\n5)Укр.лит.\n6)Химия\n7)Физ-ра\n---Четверг:\n1)История\n2)Биология\n3)Геометрия\n4)Укр.лит.\n5)Англ.мова\n6)ДУМ(Химия)\n---Пятница:\n1)История\n2)Укр.мова\n3)Заруб.лит.\n4)Физ-ра\n5)Физика\n(Некоторые предметы могут меняться по неделям или быть у того или другого направление, поэтому случаю я буду уведомлять команде "событие") ')

@bot.message_handler(commands=['clock'])
def start_message(message):
    bot.send_message(message.chat.id, '1)8:00-8:45\n2)8:55-9:40\n3)9:55-10:40\n4)10:55-11:40\n5)11:50-12:35\n6)12:50-13:35\n7)13:45-14:30')

@bot.message_handler(commands=['menu'])
def start_message(message):
    bot.send_message(message.chat.id, 'Команды, которыми ты можешь воспользоваться:\n/homework-Доманее задание;\n/event-какие-то намечающиеся события;\n/timetable-расписание уроков и аудитории, где будут проходить уроки;\n/clock-расписание звонков;\n/menu-Вернуться назад к командам;\n(Некоторые функции могут добавляться со временем, и ты можешь подказать какую ту функцию добавить, а мой создатель подумает над этим)')

bot.polling()