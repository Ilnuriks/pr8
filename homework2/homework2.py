while True:
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        sum = num1 + num2
        print("Сумма:", sum)
    except ValueError:
        print("Ошибка! Введите целые числа.")


