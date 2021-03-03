import re

from user import User


def username_validation():
    while True:
        name = input('enter username')
        if len(name.split(' ')) > 2 and name.split(' ')[-1] != '' and name.split(' ')[0] != '':
            return name
        else:
            print('Enter correct name and surname')


def nickname_validation():
    return input('enter nickname')


def mail_validation():
    while True:
        mail = input('enter mail')
        if re.search(r'(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6})', mail):
            return mail
        else:
            print('Enter correct email')


def password_confirm(password):
    while True:
        re_password = input('Re-enter password:')
        if re_password == password:
            return re_password
        else:
            print('Password mismatch')


def password_validation():
    while True:
        password = input('Enter password')
        if re.search(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15})', password):
            return password_confirm(password)
        else:
            print('Password must be at least 8 characters long,\n'
                  'contain one or more capital letters,\n'
                  'one or more small letters,\n'
                  'one or more numbers')


def create_new(data, save_data):
    user_id = (len(data.keys()) + 1)
    username = username_validation()
    user_nickname = nickname_validation()
    user_mail = mail_validation()
    user_password = password_validation()
    user_tasks = {}

    new_user = User(user_id, username, user_nickname, user_mail, user_password, user_tasks)
    data[new_user.mail] = new_user.get_user_data()
    save_data(data)
