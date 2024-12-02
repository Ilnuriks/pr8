while True:
    try:
        a = int(input("Введите первое число (a): "))
        b = int(input("Введите второе число (b): "))
        break # Выход из цикла, если ввод корректный
    except ValueError:
        print("Ошибка! Введите только целые числа.")

start = int(min(a, b))
end = int(max(a, b))

for i in range(start + 1, end):
    print(i)

