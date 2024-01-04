class Car:
    _year: int = 1970 #В питоне нет возможности определить модификатор доступа свойства или метода
    __model: str = ''
    make: str = ''
    color: str = ''

    def __init__(self, year: int, model: str, make: str, color: str) -> None:
        self._year = year
        self.make = make
        self.__model = model
        self.color = color

    def print_all(self) -> None:
        print(self._year, self.make, self.__model, self.color)


class BMW(Car):  # Наследуем от Car
    is_M_model: bool = False

    def print_all(self) -> None: #Переопределяем метод
        print("Информациф об объекте:", self._year, self.make, self._Car__model, self.color) #если имя свойства начинается с __, то оно доступно только внутри класса или с указанием класса


x3_car = BMW(2020, "M3", "BMW", "Blue")
x3_car.print_all()
#print(x3_car.__model) #вернет ошибку, т.к. если имя свойства начинается с __, то оно доступно только внутри класса или с указанием класса