import json

users = {}
pizzas_1 = {
    1: "Маргарита" "500",
    2: "Пепперони" "600",
    3: "Четыре сыра" "450",
    4: "Гавайская" "700",
    5: "Мясная" "668"
}
pizzas_2 = {
    1: "Четыре сезона" "525",
    2: "Карбонара" "599",
    3: "Пицца с морепродуктами" "499",
    4: "Пицца с тунцом" "625",
    5: "Ветчина и грибы" "550"
}
pizzas_3 = {
    1: "Цезарь" "479",
    2: "Барбекю" "750",
    3: "Римская пицца" "600",
    4: "Грибная пицца" "733",
    5: "Вегетарианская" "999"
}

try:

    def admin():
        global users
        login, password = input("entry login --- "), input("entry password")

        if login == "admin" and password == "12345":
            while True:

                admin_choice = input(f"""
1. показать все заказы
2. удалить заказ
3. выйти
""")
                if admin_choice == "1":
                    with open('orders.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    for key in data:
                        print(key + ':')
                        for item in data[key]:
                            print(f"   {item}: {data[key][item]}")
                        print()

                elif admin_choice == '2':
                    del_choise = input("""
1. удалить заказ по индексу
2. удалить все заказы
""")
                    if del_choise == "1":
                        user_del_name = input("введи имя чтобы удалить его заказ --- ")
                        if user_del_name in users:
                            del users[int(user_del_name)]
                        with open("orders.json", "w", encoding="utf-8") as file:
                            json.dump(users, file, ensure_ascii=False, indent=4)
                    elif del_choise == "2":
                        users = {}
                        with open("orders.json", "w", encoding="utf-8") as file:
                            json.dump(users, file, ensure_ascii=False, indent=4)
                    elif del_choise == "3":
                        pass
                    else:
                        print("введите от 1 до 3")


                elif admin_choice == '3':
                    break
                else:
                    print("введите от 1 до 3")


    def get_user_inf(user_number):
        user_name = input(f"введите имя посетителя номер: {user_number + 1} --- ")
        user_age = int(input(f"введите возраст посетителя номер: {user_number + 1} --- "))

        return {user_number: {"name": user_name,
                              "age": user_age
                              }}


    def make_order():
        users_count = int(input("сколько друзей вы взяли с собой --- "))
        if users_count > 0:
            for user_num in range(users_count):
                users.update(get_user_inf(user_num))

            for key in users:
                print(f"{key + 1} : {users[key]}")

            for key in users:
                if users[key]["age"] <= 18:
                    user_choice = int(input(f"""
Какую пиццу выберет {users[key]["name"]}

1. Маргарита 500р

2. Пепперони 600р

3. Четыре сыра 450р

4. Гавайская 700р

5. Мясная 668р
--- """))

                elif users[key]["age"] > 18 and users[key]["age"] <= 50:
                    user_choice = int(input(f"""
Какую пиццу выберет {users[key]["name"]}

1. Четыре сезона 525р

2. Карбонара 599р

3. Пицца с морепродуктами 499р

4. Пицца с тунцом 625р

5. Ветчина и грибы 550р
--- """))

                elif users[key]["age"] > 50:
                    user_choice = int(input(f"""
Какую пиццу выберет {users[key]["name"]}

1. Цезарь 479р

2. Барбекю 750р

3. Римская пицца 600р

4. Грибная пицца 733р

5. Вегетарианская 999р
--- """))

                else:
                    print("введи число из меню")

                if user_choice in [_ for _ in range(1, 6)]:
                    if users[key]["age"] <= 18:
                        users[key].update({"pizza": pizzas_1[user_choice]})
                    elif users[key]["age"] > 18 and users[key]["age"] <= 50:
                        users[key].update({"pizza": pizzas_2[user_choice]})
                    elif users[key]["age"] > 50:
                        users[key].update({"pizza": pizzas_3[user_choice]})
                    else:
                        print("это сообщение никогда не выведется ведь выше уже есть проверка на возраст")

                else:
                    print("введи число из меню")
                    return 0

        else:
            print("нет")
            return 0

        print("ваше меню")
        for key in users:
            print(f"для {users[key]['name']} : {users[key]['pizza'][:-3]}")

        pay_price = 0
        for key in users:
            pay_price += int(users[key]["pizza"][-3:])
        pay = int(input(f"""
способ оплаты:

с вас {pay_price}р

1. карта
2. наличные   
--- """))
        if pay in [1, 2]:
            if pay == 1:
                with open("orders.json", "w", encoding="utf-8") as file:
                    json.dump(users, file, ensure_ascii=False, indent=4)
                print("оплата прошла успешно")
                return 1
            elif pay == 2:
                cash = int(input(f"дайте роботу наличку (больше {pay_price})"))
                if cash < pay_price:
                    print("недостаточно средств")
                    return 2
                else:
                    with open("orders.json", "w", encoding="utf-8") as file:
                        json.dump(users, file, ensure_ascii=False, indent=4)
                    print(f"приятного аппетита!!! ваша сдача {cash - pay_price}")
                    return 1



        print(users)





except ValueError:
    print("что то пошло не так")


while True:
    try:
        choice = input("""
1. make an order
2. entry by admin
3. exit
""")
        if choice == '1':
            make_order()
        elif choice == '2':
            admin()
        elif choice == '3':
            break
        elif choice == '5':
            print(users)
    except ValueError:
        print("введи число от 1 до 4")






