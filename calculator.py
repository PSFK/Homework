def calculator():
    print("Добро пожаловать в калькулятор!")

    while True:
        try:
            # Запрос ввода первого числа
            first_number = float(input("Введите первое число: "))

            # Запрос арифметического знака
            operation = input("Введите арифметический знак (+, -, *, /): ").strip()
            if operation not in {'+', '-', '*', '/'}:
                print("Некорректный арифметический знак. Попробуйте снова.")
                continue

            # Запрос ввода второго числа
            second_number = float(input("Введите второе число: "))

            # Проверка деления на ноль
            if operation == '/' and second_number == 0:
                print("Ошибка: Делить на ноль нельзя. Попробуйте снова.")
                continue

            # Выполнение операции
            if operation == '+':
                result = first_number + second_number
            elif operation == '-':
                result = first_number - second_number
            elif operation == '*':
                result = first_number * second_number
            elif operation == '/':
                result = first_number / second_number

            print(f"Результат: {result}")

            # Запрос на продолжение работы
            continue_choice = input("Хотите выполнить еще одну операцию? (да/нет): ").strip().lower()
            if continue_choice not in {'да', 'д', 'yes', 'y'}:
                print("Спасибо за использование калькулятора. До свидания!")
                break

        except ValueError:
            print("Ошибка: Введены некорректные данные. Убедитесь, что вводите числа.")

# Запуск калькулятора
if __name__ == "__main__":
    calculator()
