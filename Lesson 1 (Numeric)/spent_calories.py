from decimal import Decimal


def spent_calories(
        weight: float = 75,
        height: float = 175,
        dist: float = 9.75,
        hours: float = 2,
        minutes: float = 120
) -> Decimal:
    return Decimal((0.035 * weight + (dist / hours) ** 2 / height * 0.029 * weight) * minutes)


print(
    spent_calories()
)
