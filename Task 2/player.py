from variants import Variants


class Player:
    choice = 0
    name = ""

    def __init__(self, name: str = "bot", choice: None | int = None):
        self.choice = choice if choice is not None else Variants.random_variant(Variants)
        self.name = name

    def who_wins(self, first, second):
        if first.choice == second.choice:
            return "Ничья"
        elif first.choice == Variants.Scissors:
            if second.choice == Variants.Rock:
                return second.name
            elif second.choice == Variants.Paper:
                return first.name
        elif first.choice == Variants.Rock:
            if second.choice == Variants.Scissors:
                return first.name
            elif second.choice == Variants.Paper:
                return second.name
        elif first.choice == Variants.Paper:
            if second.choice == Variants.Rock:
                return first.name
            elif second.choice == Variants.Scissors:
                return second.name


