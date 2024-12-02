sum = 0
while True:
    user_input = input("Введите число ('stop' или 'end' для завершения): ")
    
    if user_input.lower() in ["stop", "end"]:
        break # Выход из цикла, если введены 'stop' или 'end'
    else:
        try:
            num = float(user_input) 
            sum += num
        except ValueError:
            print("Ошибка! Введите число или 'stop'/'end'.")

print("Сумма введенных чисел:", sum)