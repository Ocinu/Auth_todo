"""
Задание #1:
Написать регистрацию и авторизацию пользователей. Данные нужно хранить в файле users.json.
При регистрации запрашиваем следующие поля:
1) ФИО пользователя. Нужно проверить, что он ввел три или больше слов.
2) Ник пользователя
3) Почта пользователя. Нужно проверить на правильность ввода почти и проверку на то, что пользователей с такой почтой нет в базе.
4) Пароль. Нужно проверить пароль на:
 - Одна или больше больших букв в пароле
 - Одна или больше маленьких букв в пароле
 - Одна или больше цифр в пароле
 - Длина пароля больше 8
 - Есть ли спец. символы в пароле
5) Повторить пароль. Проверить, что пароль совпадает с ранее введенным.
У каждого пользователя должен быть уникальный ИД (Номер), для каждого нового пользователя этот ид = ид_прошлого_пользователя + 1
После регистрации записать пользователя в базу.

При авторизации запрашиваем следующие поля:
1) Почта пользователя. Нужно проверить на правильность ввода почти и проверку на то, что пользователей с такой почтой есть в базе.
2) Пароль. Нужно проверить, что пароль подходит к пользователю с такой почтой.
После авторизации вывести приветственное сообщение.

Если пользователь вводит что-то неправильно, то запрашиваем до тех пор, пока не введет правильно!

Задание #2:
Написать TODO-лист (Список дел)
В приложении должна быть возможность:
1) Добавить дела. Поля:
 - Дата выполнения
 - Название
 - Описание
 - Приоритет
2) Изменение дела:
 - Дата выполнения
 - Название
 - Описание
 - Приоритет
3) Удаление дела

Нужно использовать регистрацию/авторизацию из прошлого задания.
Пользователь должен видеть только свои дела. У каждого дела есть поле user_id - номер пользователя который его создал
Все дела необходимо сохранять в файл todo.json
"""
from new_user import create_new
from user_tasks import user_tasks
from user import User
import json

USERS = 'users.json'


def load_data():
    try:
        with open(USERS, 'r') as f:
            return json.load(f)
    except IOError:
        f = open(USERS, 'w+')
        f.close()
        return {}


def save_data(data):
    with open(USERS, 'w') as f:
        f.write(json.dumps(data))


def load_valid_user(data):
    while True:
        user_password = input('Enter your password: ')
        if user_password != data['Password']:
            print('wrong password')
        else:
            current_user = User(data['user_id'],
                                data['Name'],
                                data['Nickname'],
                                data['Email'],
                                data['Password'],
                                data['tasks'])
            print(current_user.get_user_info())
            print(current_user.get_user_tasks())
            return user_tasks(current_user)


def start():
    user_list = load_data()
    init_request = input('Enter your email: ')
    if init_request in user_list.keys():

        user_list[init_request] = load_valid_user(user_list[init_request])
        save_data(user_list)
    else:
        choice = input('Your email is not on the list\n'
                       'create a new one - enter 1\n'
                       'or re-enter email - enter 2')
        if choice == '1':
            create_new(user_list, save_data)
            start()
        else:
            start()


if __name__ == '__main__':
    start()
