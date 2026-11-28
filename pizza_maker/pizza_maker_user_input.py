def admin_sing_in():
        login, password = input("entry login --- "), input("entry password")
        if login == "admin" and password == "12345":
            return True
        else:
            return False, "wrong password"

def admin_choice_inp():
    admin_choice = input(f"""
1. показать все заказы
2. удалить заказ
3. выйти
""")
    return admin_choice

def admin_del_choice():
    del_choice = input("""
1. удалить заказ по индексу
2. удалить все заказы
""")
    return del_choice

def admin_del_index():
    user_del_index = input("введи индекс чтобы удалить его заказ --- ")
    return user_del_index

def input_user_inf(user_number):
    user_name = input(f"введите имя посетителя номер: {user_number + 1} --- ")
    user_age = int(input(f"введите возраст посетителя номер: {user_number + 1} --- "))
    return user_name, user_age

def input_users_count():
    users_count = int(input("сколько друзей вы взяли с собой --- "))
    return users_count

def user_menu_choice():
    user_choice = int(input("твой выбор из меню --- "))
    return user_choice

def input_payment_method(pay_price):
    pay = int(input(f"""
способ оплаты:

с вас {pay_price}р

1. карта
2. наличные   
--- """))
    return pay

def input_give_cash(pay_price):
    pay_choice = int(input(f"дайте роботу наличку (больше {pay_price})"))
    return pay_choice

def input_main_choice():
    choice = input("""
1. make an order
2. entry by admin
3. exit
""")
    return choice
