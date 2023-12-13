def sum_of_digits(number_str):
    if not number_str.isdigit():
        print("Ошибка: Введите строку, представляющую целое положительное число.")
        return None

    total_sum = sum(int(digit) for digit in number_str)
    return total_sum

input_str = input("Введите строку, представляющую целое положительное число: ")

result = sum_of_digits(input_str)

if result is not None:
    print("Сумма цифр числа:", result)