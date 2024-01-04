def get_integer_from_user() -> int:
    input_data = input("Введите целое число: ")

    try:
        return int(input_data)
    except ValueError:
        print("Введено некорректное значение!")
        return get_integer_from_user()


a = get_integer_from_user()
b = get_integer_from_user()

print(a + b)
