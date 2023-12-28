def print_distance_and_calories(
        weight: float = 75,
        height: float = 175,
        steps: int = 8462,
        hours: float = 2,
        step_length: float = 0.65
) -> None:
    distance = steps * step_length / 1000

    mean_speed = distance / hours

    spent_calories = (0.035 * weight + (mean_speed ** 2 / height) * 0.029 * weight) * hours * 60

    output = f"{distance} {spent_calories}"

    print(output)


print_distance_and_calories()
