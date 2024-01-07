from variants import Variants
from player import Player

bot = Player("bot")
alex = Player("alex")
petr = Player("petr", Variants.Scissors)

print(
    bot.who_wins(bot, alex)
)

print(
    bot.who_wins(alex, petr)
)
