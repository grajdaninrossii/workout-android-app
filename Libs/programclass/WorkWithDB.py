
import sqlite3



# --------------------------------------------------------------- Конфиг ---------------------------------------------------------------


class WorkWithDB():
    def __init__(self):
        self.connect = sqlite3.connect('alphadynamics.db')
        self.cursor = self.connect.cursor()

    # --------------------------------------------------------------- Конфиг ---------------------------------------------------------------

    def convert_to_binary_data(self, filename):  # Преобразование данных в двоичный формат
        with open(filename, 'rb') as file:
            blob_data = file.read()
        return blob_data

    # ----------------------------------------------------- Функции создания таблиц --------------------------------------------------------

    def addTable_users(self):    # Создание таблицы USERS: (phone, password, email, name, gender, birthday)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT,
            password TEXT,
            email TEXT,
            name TEXT,
            gender TEXT,
            birthday TEXT);
        """)
        self.connect.commit()

    def addTable_publications(self):    # Создание таблицы PUBLICATIONS: (header, body, photo)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS publications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            header TEXT,
            body TEXT,
            photo TEXT);
        """)
        self.connect.commit()



    # ------------------------------------------------- Функции связанные с пользователем ------------------------------------------------------------

    def autorization(self, email, password):        # Авторизация по телефону и паролю
        self.cursor.execute(f"""SELECT id, email, password FROM users WHERE email = '{email}';""")
        user = self.cursor.fetchone()
        # print(user)
        if user is None:
            return 1 # Такого логина не существует или пароль неверный
        elif password != user[2]:
            return 1
        else:
            return 0 # Авторизация прошла успешно

    def addUser(self, data):    # Формат добавления пользователя: массив(телефон, пароль, емаил, имя, гендер, дата рождения)
        # Проверка, есть ли такой логин уже.
        self.cursor.execute(f"""SELECT id, email, password FROM users WHERE email = '{data[2]}';""")
        user = self.cursor.fetchone()
        if user is None:
            self.cursor.execute("""INSERT INTO users(phone, password, email, name, gender, birthday)
                VALUES(?, ?, ?, ?, ?, ?);""", data)
            self.connect.commit()
            return 0 # Регистрация прошла успешно
        else:
            return 1 # Ошибка! Такой пользователь уже зарегистрирован!



    def updateUser(self, attribute, value, id):     # Формат обновления данных пользователя: attribute - это один из параметров(phone, password, email, name, gender, birthday)
                                                    # value - значение на которое нужно изменить атрибут и id - ID пользователя
        self.cursor.execute("""UPDATE users SET """ + attribute + """=""" + value + """ WHERE id=""" + id +""";""")
        self.connect.commit()

    def deleteUser(self, id):    # Удаление пользователя по его ID
        self.cursor.execute("""DELETE FROM users WHERE id=?;""", id)
        self.connect.commit()

    # ------------------------------------------------- Функции связанные с пользователем ------------------------------------------------------------


    # --------------------------------------------------- Функции связанные со статьями --------------------------------------------------------------

    def giveID(self, header):        # Получение ID статьи
        self.cursor.execute("""SELECT (id, header) FROM publications;""")
        all_publics = self.cursor.fetchall()
        isError = 0
        for row in all_publics:
            if row[1] == header:
                id = row[0]
                isError = 1
        if isError == 1:
            return id         # Возвращает ID публикации
        else:
            return 0          # Возвращает 0, это значит, что публикация не найдена

    def addPublication(self, data):    # Создание статьи
                                       # Формат массива data: header - текст заголовка; body - текст статьи: photo - название файла фотографии

        # binary_photo = self.convert_to_binary_data(data[2])
        # data[2] = binary_photo
        # print(data)

        self.cursor.execute("""INSERT INTO publications(header, body, photo)
            VALUES(?, ?, ?);""", data)
        self.connect.commit()

    # def updatePublication(self, data):    # Изменение статьи
    #                                       # Формат массива data: id - (обязательный параметр) ID статьи; header - текст заголовка; body - текст статьи: photo - название файла фотографии
    #
    #     id = data[0]
    #
    #     if data[3] != '':
    #         binary_photo = self.convert_to_binary_data(data[3])
    #         self.cursor.execute("UPDATE publications SET photo=" + binary_photo + " WHERE id=" + id +""";""")
    #
    #     if data[1] != '':
    #         self.cursor.execute("""UPDATE publications SET header=""" + data[1] + """ WHERE id=""" + id +""";""")
    #
    #     if data[2] != '':
    #         self.cursor.execute("""UPDATE publications SET body=""" + data[2] + """ WHERE id=""" + id +""";""")
    #
    #     self.connect.commit()
    #
    # def deletePublication(self, id):    # Удаление статьи по ID
    #
    #     self.cursor.execute("""DELETE FROM publications WHERE id=?""", id)
    #     self.connect.commit()

    def outPublication(self, id):

        self.cursor.execute(f"SELECT id, header, body, photo FROM publications WHERE id = {id};")
        one_result = self.cursor.fetchall()
        return one_result

    # --------------------------------------------------- Функции связанные со статьями --------------------------------------------------------------
