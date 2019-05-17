# coding:utf-8
password_list = ['*#*#', '12345']


def account_login():
    times = 0
    while times <= 2:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_correct:
            print('Login success!')
        elif password_reset:
            new_password = input('New password:')
            password_list.append(new_password)
            print('Your new password has changed successfully!')
            account_login()
        else:
            print('Wrong password or invalid input!')
            times = times + 1
    else:
        print('Your account has been suspended')


account_login()
