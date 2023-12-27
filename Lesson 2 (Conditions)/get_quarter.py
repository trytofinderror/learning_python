def get_quarter(
        x: float = 0,
        y: float = 0
) -> str:
    if x > 0 and y > 0:
        return "Первая четверть"
    elif x < 0 and y > 0:
        return "Вторая четверть"
    elif x > 0 and y < 0:
        return "Четвертая четверть"
    elif x < 0 and y < 0:
        return "Третья четверть"
    else:
        return "X и Y должны быть отличны от нуля"


print(
    get_quarter(3, -1)
)
