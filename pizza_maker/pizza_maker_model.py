import json
import asyncio
from pizza_maker import pizza_maker_user_input as ui

cheese = 5000
order = {}
pizzas_1 = {
    1: ["Маргарита", 500, {"сыр": 1}],
    2: ["Пепперони", 600, {"сыр": 1}],
    3: ["Четыре сыра", 450, {"сыр": 5}],
    4: ["Гавайская", 700, {"сыр": 1}],
    5: ["Мясная", 668, {"сыр": 1}],
    6: ["сок яблочный", 668, {"яблоко": 1}]
}
pizzas_2 = {
    1: ["Четыре сезона", 525, {"сыр": 1}],
    2: ["Карбонара", 599, {"сыр": 1}],
    3: ["Пицца с морепродуктами", 499, {"сыр": 1}],
    4: ["Пицца с тунцом", 625, {"сыр": 1}],
    5: ["Ветчина и грибы", 550, {"сыр": 1}],
    6: ["кола", 668, {"кола": 1}]
}
pizzas_3 = {
    1: ["Цезарь", 479, {"сыр": 1}],
    2: ["Барбекю", 750, {"сыр": 1}],
    3: ["Римская пицца", 600, {"сыр": 1}],
    4: ["Грибная пицца", 733, {"сыр": 1}],
    5: ["Вегетарианская", 999, {"сыр": 1}],
    6: ["водичка из под пельменей", 668, {"кола": 1}]
}

try:

    def key_rename(dict1, key):

        lst1 = [i for i in dict1]
        lst2 = [dict1[i] for i in dict1]
        res = {}
        for i in range(len(dict1)):
            if lst1[i] == key:
                res.update({int(lst1[i]) - 1: lst2[i]})
            else:
                res.update({lst1[i]: lst2[i]})
        return res


    def decor_check(input_func):
        def outer_func(price):
            print(10*"*", end="")
            input_func(price)
            print(10*"*")
        return outer_func

    @decor_check
    def print_check(price):
        print(f"""
чек
продавец: --- ""
цена --- {price}
скидка 0%
ИТОГО {price}р""")


    async def admin():
        global order

        if ui.admin_sing_in():
            while True:

                admin_choice = ui.admin_choice_inp()
                if admin_choice == "1":
                    with open('orders.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    for key in data:
                        print(key + ':')
                        for item in data[key]:
                            print(f"   {item}: {data[key][item]}")
                        print()

                elif admin_choice == '2':
                    del_choice = ui.admin_del_choice()
                    if del_choice == "1":
                        user_del_index = ui.admin_del_index()
                        with open('orders.json', 'r', encoding='utf-8') as file1:
                            data = json.load(file1)
                            if user_del_index in data:
                                del data[user_del_index]
                            for i in data:
                                if i > user_del_index:
                                    data = key_rename(data, i)

                        with open("orders.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, ensure_ascii=False, indent=4)
                    elif del_choice == "2":
                        order = {}
                        with open("orders.json", "w", encoding="utf-8") as file:
                            json.dump(order, file, ensure_ascii=False, indent=4)
                    elif del_choice == "3":
                        pass
                    else:
                        print("введите от 1 до 3")

                elif admin_choice == '3':
                    break
                else:
                    print("введите от 1 до 3")


    async def get_user_inf(user_number):
        user_name, user_age = ui.input_user_inf(user_number)

        return {user_number: {"name": user_name,
                              "age": user_age,
                              "pizza": []
                              }}


    async def make_order():
        users_count = ui.input_users_count()
        if users_count > 0:
            for user_num in range(users_count):
                order.update(await get_user_inf(user_num))

            for key in order:
                print(f"{key + 1} : {order[key]}")

            for key in order:
                if order[key]["age"] <= 18:
                    print(f"Какую пиццу выберет {order[key]["name"]}")
                    for i in pizzas_1:
                        print(f"{i}. {pizzas_1[i][0]} - {pizzas_1[i][1]}р")
                    user_choice = ui.user_menu_choice()

                elif order[key]["age"] > 18 and order[key]["age"] <= 50:
                    print(f"Какую пиццу выберет {order[key]["name"]}")
                    for i in pizzas_2:
                        print(f"{i}. {pizzas_2[i][0]} - {pizzas_2[i][1]}р")
                    user_choice = ui.user_menu_choice()

                elif order[key]["age"] > 50:
                    print(f"Какую пиццу выберет {order[key]["name"]}")
                    for i in pizzas_3:
                        print(f"{i}. {pizzas_3[i][0]} - {pizzas_3[i][1]}р")
                    user_choice = ui.user_menu_choice()

                else:
                    print("введи число из меню")

                if user_choice in [_ for _ in range(1, 7)]:
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

        print("ваш заказ:")
        for key in order:
            print(f"для {order[key]['name']} : {order[key]['pizza'][0]}")

        cheese_price = 0
        pay_price = 0
        for key in order:
            cheese_price += int(order[key]["pizza"][2]["сыр"]) if "сыр" in order[key]["pizza"][2] else 0
            pay_price += int(order[key]["pizza"][1])
        pay = ui.input_payment_method(pay_price)

        if pay in [1, 2]:
            if pay == 1:
                with open("orders.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                    length = len(data)
                    data.update({length: order})
                with open("orders.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                with open("products.json", "r", encoding="utf-8") as file_1:
                    data = json.load(file_1)
                with open("products.json", "w", encoding="utf-8") as file_1:
                    data["сыр"] = data["сыр"] - cheese_price
                    json.dump(data, file_1, ensure_ascii=False, indent=4)


                print_check(pay_price)
                print("оплата прошла успешно")
                return 1
            elif pay == 2:
                cash = ui.input_give_cash(pay_price)
                if cash < pay_price:
                    print("недостаточно средств")
                    return 2
                else:
                    with open("orders.json", "r", encoding="utf-8") as file:
                        data = json.load(file)
                        length = len(data)
                        data.update({length: order})
                    with open("orders.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                    with open("products.json", "r", encoding="utf-8") as file1:
                        data = json.load(file1)
                    with open("products.json", "w", encoding="utf-8") as file_1:
                        data["сыр"] = data["сыр"] - cheese_price
                        json.dump(data, file_1, ensure_ascii=False, indent=4)
                    print_check(pay_price)
                    print(f"приятного аппетита!!! ваша сдача {cash - pay_price}")

                    return 1

        print(order)





except ValueError:
    print("что то пошло не так")


async def main():
    while True:
        try:
            choice = ui.input_main_choice()
            if choice == '1':
                await make_order()
            elif choice == '2':
                await admin()
            elif choice == '3':
                break
            elif choice == '5':
                print(order)
        except ValueError:
            print("введи число от 1 до 4")


asyncio.run(main())
