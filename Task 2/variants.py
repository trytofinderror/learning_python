import random


class Variants:
    Scissors = 0
    Paper = 1
    Rock = 2

    def random_variant(self):
        return random.choice([self.Scissors, self.Paper, self.Rock])
