# Бот-помощник для школы
# @SchoolHelpBot
# 6913287200:AAEedAo9sie21yjH3Hw0VGdHBV-BIqCp-Co

# Бот должен иметь определённую тематику (магазин, блог и т.д.), форматированные сообщения (жирный, курсив, ссылка) и 3-5 различных команд.

# Запроси у пользователя имя для бота (никнейм) и проверь его по следующим критериям:
#
# 1. Длина имени не более 20 символов
# 2. Имя не начинается с цифры
# 3. Имя заканчивается на слово bot (используя стандартные методы строк, без среза)

# Если никнейм проходит проверку, выводится "Ник одобрен!", а иначе выходит сообщение с ошибкой в нике.

import telebot
import math
bot = telebot.TeleBot('6913287200:AAEedAo9sie21yjH3Hw0VGdHBV-BIqCp-Co')
@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, '<b>Это бот-помощник для школы</b>', parse_mode='HTML')
    send_commands(message)

def send_commands(message):
    bot.send_message(message.chat.id, '<u>Доступные команды:</u>\n• <code>Пифагор</code>\n• <code>Дискриминант</code>\n• <code>Треугольник</code>\n• <code>Физика</code>\n• <code>Имя бота</code>', parse_mode='HTML')

@bot.message_handler()
def get_message(message):
    match message.text.lower():
        case 'пифагор':
            mess = bot.send_message(message.chat.id, 'Найти стороны прямоугольного треугольника по теореме Пифагора.\nВпиши 2 числа и х (неизвестная сторона) через пробел, первые два - катеты, третье - гипотенуза. "3 х 5" означает, что первый катет равен 3, второй катет неизвестен, а гипотенуза равна 5')
            bot.register_next_step_handler(mess, pifagor)
        case 'дискриминант':
            mess = bot.send_message(message.chat.id, 'Найти корни квадратного уравнения по коэффициентам через дискриминант, если левая часть приравнена к нулю и в ней все математические операции посчитаны. \nПишешь боту коэффициенты через пробел, десятичные дроби через точку, и он выдает дискриминант и корни, если они есть')
            bot.register_next_step_handler(mess, discriminant)
        case 'треугольник':
            mess = bot.send_message(message.chat.id, 'Найти все углы треугольника, их синусы и косинусы, и площадь если известны 3 стороны\nВпиши 3 числа через пробел и бот 3 раза напишет угол, который лежит напротив этой стороны, его косинус и синус. В конце бот посчитает площадь')
            bot.register_next_step_handler(mess, triangle)
        case 'физика':
            bot.send_message(message.chat.id, '<b>Это база материалов для подготовки к ОГЭ по физике от Макса Кораблёва:</b> https://base-of-physics-by-max-korablev.notion.site/44c8377b595f44bd844d8ba4cfef16f6',parse_mode='HTML')
            send_commands(message)
        case 'имя бота':
            mess = bot.send_message(message.chat.id, '<b>Бот проверит имя для бота по следующим критериям:</b>\n1. Длина имени не более 20 символов\n2. Имя не начинается с цифры\n3. Имя заканчивается на слово bot',parse_mode='HTML')
            bot.register_next_step_handler(mess, name_bot)
def pifagor(message):
    list = message.text.split(' ')
    cat1, cat2, hyp = list[0], list[1], list[2]
    if cat1 == 'x' or cat1 == 'х':
        cat1 = (float(hyp)**2-float(cat2)**2)**0.5
        bot.send_message(message.chat.id, f'<b>Неизвестная сторона: {round(cat1, 4)}</b>', parse_mode='HTML')
        send_commands(message)
    elif cat2 == 'x' or cat2 == 'х':
        cat2 = (float(hyp)**2-float(cat1)**2)**0.5
        bot.send_message(message.chat.id, f'<b>Неизвестная сторона: {round(cat2, 4)}</b>', parse_mode='HTML')
        send_commands(message)
    elif hyp == 'x' or hyp == 'х':
        hyp = (float(cat2)**2+float(cat1)**2)**0.5
        bot.send_message(message.chat.id, f'<b>Неизвестная сторона: {round(hyp, 4)}</b>', parse_mode='HTML')
        send_commands(message)
def discriminant(message):
    list = message.text.split(' ')
    a, b, c = float(list[0]), float(list[1]), float(list[2])
    d = b**2-4*a*c
    bot.send_message(message.chat.id, f'Дискриминант: {round(d,5)}')
    if d > 0:
        x1 = (b*(-1)+d**0.5)/2*a
        x2 = (b*(-1)-d**0.5)/2*a
        bot.send_message(message.chat.id, f'<b>Первый корень: {round(x1,5)}\nВторой корень: {round(x2,5)}</b>', parse_mode='HTML')
    if d == 0:
        x = b*(-1)/2*a
        bot.send_message(message.chat.id, f'<b>Корень: {round(x,5)}</b>', parse_mode='HTML')
    if d < 0:
        bot.send_message(message.chat.id, '<b>Корней нет</b>', parse_mode='HTML')
    send_commands(message)
def triangle(message):
    list = message.text.split(' ')
    a, b, c = float(list[0]), float(list[1]), float(list[2]),

    cosalpha = (a**2-c**2-b**2)/(-2*c*b)
    sinalpha = (1 - cosalpha**2)**0.5
    alpharad = math.acos(cosalpha)
    alphadeg = alpharad*180/math.pi
    bot.send_message(message.chat.id, f'Угол напротив стороны, которая равна {a}:  <b>{round(alphadeg, 3)}</b>\nЕго косинус:  <b>{round(cosalpha,4)}</b>\nЕго синус:  <b>{round(sinalpha,4)}</b>', parse_mode='HTML')

    cosbetta = (b**2-a**2-c**2)/(-2*a*c)
    sinbetta = (1 - cosbetta ** 2) ** 0.5
    bettarad = math.acos(cosbetta)
    bettadeg = bettarad * 180 / math.pi
    bot.send_message(message.chat.id, f'Угол напротив стороны, которая равна {b}:  <b>{round(bettadeg, 3)}</b>\nЕго косинус:  <b>{round(cosbetta,4)}</b>\nЕго синус:  <b>{round(sinbetta,4)}</b>', parse_mode='HTML')

    cosgamma = (c**2-a**2-b**2)/(-2*a*b)
    singamma = (1 - cosgamma**2)**0.5
    gammarad = math.acos(cosgamma)
    gammadeg = gammarad * 180 / math.pi
    bot.send_message(message.chat.id, f'Угол напротив стороны, которая равна {c}:  <b>{round(gammadeg, 3)}</b>\nЕго косинус:  <b>{round(cosgamma, 4)}</b>\nЕго синус:  <b>{round(singamma, 4)}</b>', parse_mode='HTML')

    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    bot.send_message(message.chat.id, f'Площадь треугольника: <b>{round(s, 3)}</b>',parse_mode='HTML')

    send_commands(message)
def name_bot(message):
    name = message.text
    if len(name) <= 20:
        try:
            int(name[0])
        except ValueError:
            if name[-3:] == 'bot':
                bot.send_message(message.chat.id, 'Ник одобрен!')
            else:
                bot.send_message(message.chat.id, 'Ник должен заканчиваться на "bot"')
        else:
            bot.send_message(message.chat.id, 'Ник не должен начинаться с цифры')
    else:
        bot.send_message(message.chat.id, 'Длина ника должна быть не более 20 символов')


bot.infinity_polling()