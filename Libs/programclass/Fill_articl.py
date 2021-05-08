from WorkWithDB import WorkWithDB

# Создание базы данных(таблицы для статей)
def create_art():

    db = WorkWithDB()
    db.addTable_publications()
    for i in range(1,8):
        f = open(f"/home/miroslav/Documents/kivy_project/Libs/programclass/text/art{i}.txt", "r")
        title = f.readline()
        body = f.read()
        image = f"Data/Images/{i}.jpg"
        data_publication = [title, body, image]
        db.addPublication(data_publication)
        f.close()

# Создание базы данных(таблицы пользователей)
def creat_users():
    db = WorkWithDB()
    db.addTable_users()
    email = "MiraImba"
    password = "r1r1"
    phone = "89180702210"
    data = [phone, password, email, "no", "no", "no"]
    db.addUser(data)


# Достаем значения из базы данных
def out_art():
    db = WorkWithDB()
    print(db.outPublication(7))



def main():
    create_art()
    creat_users()
    out_art()

main()
