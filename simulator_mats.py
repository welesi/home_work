user_pass = 123
admin_pass = 123
user_login = 'admin'
admin_login = 'admin'
if user_pass == admin_pass:
    if user_login == admin_login:
        print('Доступ полчен')
    else:
        print('Доступ запрещён')
else:
    print('Доступ запрещён')