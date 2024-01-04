class Car:
    year: int = 1970
    model: str = ''
    make: str = ''
    color: str = ''

    def __init__(self, year: int, model: str, make: str, color: str) -> None:
        self.year = year
        self.make = make
        self.model = model
        self.color = color

    def print_all(self) -> None:
        print(self.year, self.make, self.model, self.color)


class BMW(Car):  # Наследуем от Car
    is_M_model: bool = False

    def print_all(self) -> None: #Переопределяем метод
        print("Информациф об объекте:", self.year, self.make, self.model, self.color)


x3_car = BMW(2020, "M3", "BMW", "Blue")
x3_car.print_all()
