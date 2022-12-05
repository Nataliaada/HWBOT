# Создать Телефонный справочник с возможностями работы с информацией, и экспорта информации в телеграмм бот

import log
import telebot
import BD as ST

connection = ST.create_connection("list1.db")

API_TOKEN = '5952228267:AAGKH1pZLPOj9REbwvv3_CPyyxuJdWuZjsk'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f'Привет, *{message.from_user.first_name}!*\nВ любой непонятной ситуации введи\nкоманду: /help\nДа! кнопки скоро появятся ;)\nЧтобы вызвать главное меню введи: /main')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'/start - начать сначала (перезапустить бота)\n/main - главное меню\n/help - вызвать справку')


name_it = ''
num = ''
surname = ''


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/main':
        bot.send_message(message.chat.id, f'Выбери пункт меню, введя соответствующую команду: \n1: Поиск  телефона по имени\n \
    2: Посмотреть ФИ по номеру телефона \n \
    3: Добавить \n \
    4: Удалить \n \
    5: Вывести весь список  \n \
    6: Выход\n ')
        # cr.init_data_base('base_phone.csv')

    elif message.text == '/1':

        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, find_name)

    elif message.text == '/2':

        bot.send_message(message.chat.id, f'Введите номер  телефона')
        bot.register_next_step_handler(message, find_by_phone)

    elif message.text == '/3':

        bot.send_message(message.chat.id, f"Введите как в примере:('Иванов', 'Олег', '125457', '1222@bk.ru')")
        bot.register_next_step_handler(message, insert)

    elif message.text == '/4':

        bot.send_message(message.chat.id, f'Введите фамилию человека , которого нужно удалить из справочника')
        bot.register_next_step_handler(message, del_surname)

    elif message.text == '/5':
        result =bot.send_message(message.chat.id, ''.join(str(ST.execute_read_query())))
        log.result_log(message.text, result.text)
    elif message.text == '/6':
        result =bot.send_message(message.chat.id, f'Пока!!!')
        log.result_log(message.text, result.text)

    else:
        bot.send_message(
            message.chat.id, f'Я тебя не понимаю. Введи: /help.')


def find_name(message):
    global name_it
    name_it = message.text
    result = bot.send_message(message.chat.id, f'{ST.find(st=name_it)}')
    log.result_log(message.text, result.text)

def find_by_phone(message):
    global num
    num = message.text
    result = bot.send_message(message.chat.id, f'{ST.find_by_phone(st=num)}')
    log.result_log(message.text, result.text)

def insert(message):
    text = message.text
    result =  bot.send_message(message.chat.id, f'"Записи успешно вставлены в таблицу " {ST.insert(text)}')
    log.result_log(message.text, result.text)

def del_surname(message):
    global surname
    surname = message.text
    result = bot.send_message(message.chat.id, f'"Записи успешно удалены из таблицы" {ST.delete(surname)}')
    log.result_log(message.text, result.text)


bot.polling(none_stop=True, interval=0)
