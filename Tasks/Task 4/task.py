def formatted_rich_print_distance_and_calories(
        weight: float = 75,
        height: float = 175,
        steps: int = 8462,
        hours: float = 2,
        step_length: float = 0.65
) -> None:
    distance = steps * step_length / 1000

    mean_speed = distance / hours

    spent_calories = (0.035 * weight + (mean_speed ** 2 / height) * 0.029 * weight) * hours * 60

    if distance < 2:
        message = "Лежать тоже полезно. Главное — участие, а не победа!"
    elif 2 <= distance < 3.9:
        message = "Маловато, но завтра наверстаем!"
    elif 3.9 <= distance < 6.5:
        message = "Неплохо! День был продуктивным"
    else:
        message = "Отличный результат! Цель достигнута."

    output = f"""
    Сегодня вы прошли {steps} шагов. 
    Пройденная дистанция {distance} км.
    Вы сожгли {spent_calories} ккал.
    {message}"""

    print(output)


formatted_rich_print_distance_and_calories()
