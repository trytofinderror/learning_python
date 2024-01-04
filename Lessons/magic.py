class SomeClass:
    number: int = 0

    def __add__(self, other) -> None:
        print("SomeClass" + repr(other))

    def __init__(self) -> None:
        print("SomeClass initiated")

    def __str__(self) -> str:
        return "SomeClass:" + repr(self)

    def __ge__(self, other: int) -> bool:
        try:
            other = int(other)
            return self.number >= other
        except ValueError:
            print("Сравнивать можно только числа")
            return False


a = SomeClass()
print(a)
print(a >= "asd")
print(a >= -1)
