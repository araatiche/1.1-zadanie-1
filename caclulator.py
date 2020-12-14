first_number = int(input("Введите первое число: ")) # записываем ввод первого числа в переменную first_number
print("Введите символ, какую операцию хотитие выполнить.")
print("Допустимые символы операции: +, -, *, /")
operation = input("Введите символ: ") # записываем ввод символа операции в переменную operation
second_number = int(input("Введите второе число: ")) # записываем ввод второго числа в переменную second_number
#
# в зависимости от введеного символа выбераем соответствующую операцию над числами:
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0: # проверка деления на 0
        print("Деление на 0!") # если есть, выводим сообщение и выходим из программы
        exit()
    else:
        result = first_number / second_number
elif operation:
    print("Введен некоректный символ операции!") # в случае если введен некоректный символ операции выдаем соответвующее сообщение
    exit()                                       # и досрочно завершаем программу
print("Результат операции '",operation,"':",str(result)) # если все правильно выдаем результат