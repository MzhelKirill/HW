import json

order = {}
pizzas_1 = {
    1: ["Маргарита", 500],
    2: ["Пепперони", 600],
    3: ["Четыре сыра", 450],
    4: ["Гавайская", 700],
    5: ["Мясная", 668]
}
pizzas_2 = {
    1: ["Четыре сезона", 525],
    2: ["Карбонара", 599],
    3: ["Пицца с морепродуктами", 499],
    4: ["Пицца с тунцом", 625],
    5: ["Ветчина и грибы", 550]
}
pizzas_3 = {
    1: ["Цезарь", 479],
    2: ["Барбекю", 750],
    3: ["Римская пицца", 600],
    4: ["Грибная пицца", 733],
    5: ["Вегетарианская", 999]
}

try:

    def admin():
        global order
        login, password = input("entry login --- "), input("entry password")

        if login == "admin" and password == "12345":
            while True:

                admin_choice = input(f"""
1. показать все заказы
2. удалить заказы
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
                        if user_del_name in order:
                            del order[int(user_del_name)]
                        with open("orders.json", "w", encoding="utf-8") as file:
                            json.dump(order, file, ensure_ascii=False, indent=4)
                    elif del_choise == "2":
                        order = {}
                        with open("orders.json", "w", encoding="utf-8") as file:
                            json.dump(order, file, ensure_ascii=False, indent=4)
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
                              "age": user_age,
                              "pizza": []
                              }}


    def make_order():
        users_count = int(input("сколько друзей вы взяли с собой --- "))
        if users_count > 0:
            for user_num in range(users_count):
                order.update(get_user_inf(user_num))

            for key in order:
                print(f"{key + 1} : {order[key]}")

            for key in order:
                if order[key]["age"] <= 18:
                    user_choice = int(input(f"""
Какую пиццу выберет {order[key]["name"]}

1. Маргарита 500р

2. Пепперони 600р

3. Четыре сыра 450р

4. Гавайская 700р

5. Мясная 668р
--- """))

                elif order[key]["age"] > 18 and order[key]["age"] <= 50:
                    user_choice = int(input(f"""
Какую пиццу выберет {order[key]["name"]}

1. Четыре сезона 525р

2. Карбонара 599р

3. Пицца с морепродуктами 499р

4. Пицца с тунцом 625р

5. Ветчина и грибы 550р
--- """))

                elif order[key]["age"] > 50:
                    user_choice = int(input(f"""
Какую пиццу выберет {order[key]["name"]}

1. Цезарь 479р

2. Барбекю 750р

3. Римская пицца 600р

4. Грибная пицца 733р

5. Вегетарианская 999р
--- """))

                else:
                    print("введи число из меню")

                if user_choice in [_ for _ in range(1, 6)]:
                    if order[key]["age"] <= 18:
                        order[key]["pizza"] = pizzas_1[user_choice]
                    elif order[key]["age"] > 18 and order[key]["age"] <= 50:
                        order[key]["pizza"] = pizzas_2[user_choice]
                    elif order[key]["age"] > 50:
                        order[key]["pizza"] = pizzas_3[user_choice]
                    else:
                        print("это сообщение никогда не выведется ведь выше уже есть проверка на возраст")

                else:
                    print("введи число из меню")
                    return 0

        else:
            print("нет")
            return 0

        print("ваше меню")
        for key in order:
            print(f"для {order[key]['name']} : {order[key]['pizza'][0]}")

        pay_price = 0
        for key in order:
            pay_price += int(order[key]["pizza"][1])
        pay = int(input(f"""
способ оплаты:

с вас {pay_price}р

1. карта
2. наличные   
--- """))
        if pay in [1, 2]:
            if pay == 1:
                with open("orders.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                    length = len(data)
                    data.update({length: order})
                    with open("orders.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                print("оплата прошла успешно")
                return 1
            elif pay == 2:
                cash = int(input(f"дайте роботу наличку (больше {pay_price})"))
                if cash < pay_price:
                    print("недостаточно средств")
                    return 2
                else:
                    with open("orders.json", "r", encoding="utf-8") as file:
                        data = json.load(file)
                        length = len(data)
                        data.update(order)
                        with open("orders.json", "w", encoding="utf-8") as file:
                            json.dump({length: data}, file, ensure_ascii=False, indent=4)
                    print(f"приятного аппетита!!! ваша сдача {cash - pay_price}")
                    return 1



        print(order)





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
            print(order)
    except ValueError:
        print("введи число от 1 до 4")






