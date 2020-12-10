FirstNumber = int(input("Введите первое число: ")) # записываем ввод первого числа в переменную FirstNumber
print("Введите символ, какую операцию хотитие выполнить.")
print("Допустимые символы операции: +, -, *, /")
Operation = input("Введите символ: ") # записываем ввод символа операции в переменную Operation
SecondNumber = int(input("Введите второе число: ")) # записываем ввод второго числа в переменную SecondNumber
#
# в зависимости от введеного символа выбераем соответствующую операцию над числами:
if Operation == "+":
    Result = FirstNumber + SecondNumber
elif Operation == "-":
    Result = FirstNumber - SecondNumber
elif Operation == "*":
    Result = FirstNumber * SecondNumber
elif Operation == "/":
    Result = FirstNumber / SecondNumber
elif Operation:
    print("Введен некоректный символ операции!") # в случае если введен некоректный символ операции выдаем соответвующее сообщение
    exit()                                       # и досрочно завершаем программу
print("Результат операции '",Operation,"':",str(Result)) # если все правильно выдаем результат