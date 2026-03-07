import random
import time

attempt = 1

start_time = 0
end_time = 0

num1 = 0
num2 = 100
number = 0

def create_num():
    global num1, num2, number, start_time, end_time
    try:
        num1 = int(input('''задай диапазон
первое число --- '''))
        num2 = int(input('второе число --- '))

        if num1 == num2:
            print('значение твоего диапазона не корректно\nи было переведено в стандартное значение (от 1 до 100)')
            num1 = 1
            num2 = 100
        number = random.randint(num1, num2)
    except ValueError:
        print('ValueError')

    start_time = time.perf_counter()


def user_input():
    global num1, num2, number, attempt, start_time, end_time
    try:
        print(f'\nпопытка номер {attempt}')

        input_num = int(input('\nугадай число из твоего диапазона --- '))
        if input_num == number:
            end_time = time.perf_counter()
            print(f'\nты угадал загаданое число за {end_time - start_time} секунд')
        else:
            if number > input_num:
                print('\nзагаданое число больше твоего, попробуй еще раз --- ')
            else:
                print('\nзагаданое число меньше твоего, попробуй еще раз --- ')

            attempt += 1

            user_input()
    except ValueError:
        print('ValueError')


def main():
    create_num()
    user_input()


main()

