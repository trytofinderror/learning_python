from enum import Enum


class Color(Enum):
    Black = 1
    White = 2
    Red = 3
    Green = 4
    Yellow = 5


my_color = Color.Red

for color in Color:
    if color == my_color:
        print("My color is", color, "it's value is", color.value)