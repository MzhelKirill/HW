from dz_04_03_2026_2 import *

def main(num1, num2):
    choice = input('''

1 - amount
любая другая цифра - полный анализ пары чисел

НАПИШИ ЦИФРУ

''')
    try:
        num1 = int(num1)
        num2 = int(num2)
        if choice == '1':
            res = f'результат сложения - {amount(num1, num2)}'

        else:
            if num2 != 0:
                res = f'''
результат сложения: {amount(num1, num2)}
результат вычитания: {subtraction(num1, num2)}
результат умножения: {product(num1, num2)}
результат деления: {division(num1, num2)}
результат возведения в степень: {power(num1, num2)}'''
            elif choice.isdigit():
                res = f'''
результат сложения: {amount(num1, num2)}
результат вычитания: {subtraction(num1, num2)}
результат умножения: {product(num1, num2)}
ZeroDivisionError
результат возведения в степень: {power(num1, num2)}'''
            else:
                res = 'ЦИФРУ НАДО БЫЛО ПИСАТЬ'
        print(res)
    except ValueError:
        print('ValueError')


main(input('num1 --- '), input('num2 --- '))