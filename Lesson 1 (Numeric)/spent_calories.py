from decimal import Decimal

def spent_calories(
        weight=75,
        height=175,
        dist=9.75,
        hours=2,
        minutes=120
):
    return Decimal((0.035 * weight + (dist / hours) ** 2 / height * 0.029 * weight) * minutes)


print(
    spent_calories()
)
