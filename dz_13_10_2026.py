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


    def get_user_inf(user_number):
        user_name = input(f"введите имя посетителя номер: {user_number+1} --- ")
        user_age = int(input(f"введите возраст посетителя номер: {user_number+1} --- "))

        return {user_number: {"name": user_name,
                "age": user_age
                }}

    def main():
        users_count = int(input("сколько друзей вы взяли с собой --- "))
        if users_count > 0:
            for user_num in range(users_count):
                users.update(get_user_inf(user_num))

            for key in users:
                print(f"{key+1} : {users[key]}")

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
                    elif users[key]["age"]  > 18 and users[key]["age"] <= 50:
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
            print(f"для {users[key]["name"]} : {users[key]["pizza"][:-3]}")

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
                print("оплата прошла успешно")
                return 1
            elif pay == 2:
                cash = int(input(f"дайте роботу наличку (больше {pay_price})"))
                if cash < pay_price:
                    print("недостаточно средств")
                    return 2
                else:
                    print(f"приятного аппетита!!! ваша сдача {cash-pay_price}")
                    return 1

        print(users)



    main()


except ValueError:
    print("что то пошло не так")


