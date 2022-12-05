import sqlite3
from sqlite3 import Error


def create_connection(path):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(path, check_same_thread=False)
        print("База данных создана и успешно подключена к SQLite")
    except Error as error:
        print(f"Ошибка '{error}' при подключении к sqlite")
    return sqlite_connection


connection = create_connection("list1.db")


def create(query):  # Создать таблицу
    global connection
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


#
# try:
#     sqlite_create_table_LIST = '''CREATE TABLE LIST(
#          surname surname TEXT NOT NULL,
#          name surname TEXT NOT NULL,
#          telephon INTEGER NOT NULL,
#          email INTEGER NOT NULL        );'''
#     create(sqlite_create_table_LIST)
#
# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)
# finally:
#     if (connection):
#         connection.close()
#         print("Соединение с SQLite закрыто")


def insert(records):  # Добавить элементы в таблицы
    global connection
    cursor = connection.cursor()
    sqlite_insert_query = """INSERT INTO LIST
                                     (surname, name, telephon, email )
                                     VALUES (""" + records + """);"""

    cursor.execute(sqlite_insert_query)
    connection.commit()
    print("Записи успешно вставлены в таблицу LIST")
    connection.commit()
    cursor.close()


# s = input("'Иванова', 'Ольга', '553627','432@bk.ru'")
# insert(s)

# try:
#
#      s = [('Revnev ', 'Alex', '4508811', '125@bk.ru'),
#                             ('Ivanov ', 'Oleg', '5895995', '325@bk.ru'),
#                             ('Smirnov ', 'Ivan', '325457', '215@bk.ru'),
#                             ('Egorov', 'Anton', '155545', '37373bk.ru'),
#                           ('Petrov', 'Anton','1435465', '5454@bk.ru'),
#                           ('Sergeev', 'Sergey','6545464', '45545@bk.ru'),
#                           ('Ragin', 'Evgenii',' 6574635', '554544@bk.ru'),
#                           ('Vasiliev ', 'Andrey', '2645484', '455@bk.ru')]
#
# #      insert(s)
#
#
# except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
# finally:
#         if connection:
#             connection.close()
#             print("Соединение с SQLite закрыто")


def update_sqlite_table(new,old):  # Обновление/редактирование одной записи в таблице
    global connection
    try:
        cursor = connection.cursor()
        update_query = str(
            "SET  telephon = \"" + new + "\"   WHERE   telephon = \"" + old + "\"  ")  # как сделать запрос и  ввести это с клаиватуры (как input())?
        cursor.execute(update_query)
        connection.commit()
        print("Запись успешно обновлена")
        cursor.close()


    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


#
# new = input()
# old = input()
 # update_query = """Update LIST set telephon = 1 where telephon = 3"""  # как сделать запрос и  ввести это с клаиватуры (как input())?
# update_sqlite_table(new,old)


def delete(dev_id):  # удаление записей
    global connection
    try:
        cursor = connection.cursor()
        sql_update_query = " DELETE from LIST where surname LIKE \"" + dev_id + "\""
        cursor.execute(sql_update_query)
        connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)



# id = input('введите номер Id, котрый нужно удлалить из таблицы')
# delete(id)


def read_sqlite_table():
    global connection
    try:
        cursor = connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from LIST"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("Фамилия:", row[0])
            print("Имя:", row[1])
            print("Телефон", row[2])
            print("эл. почта:", row[3])
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)



# print(read_sqlite_table())


def execute_read_query():
    global connection
    cursor = connection.cursor()
    result = None
    try:
        query = "SELECT * from LIST"
        cursor.execute(query)
        result = cursor.fetchall()
        for surname in result:
            print(surname)
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# execute_read_query(connection)

def find(st):
    global connection
    cursor = connection.cursor()
    result = None
    try:
        query = "SELECT surname,name, telephon FROM LIST Where name LIKE \"" + st + "\""
        cursor.execute(query)
        result = cursor.fetchall()
        # for student in result:
        #     print(student)
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# find(connection, 'Anton')
def find_by_phone(st):
    global connection
    cursor = connection.cursor()
    result = None
    try:
        query = "SELECT surname,name, telephon FROM LIST Where telephon LIKE \"" + st + "\""
        cursor.execute(query)
        result = cursor.fetchall()
        # for student in result:
        #     print(student)
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
# st=input('bb')
# find_by_phone(str(st))
