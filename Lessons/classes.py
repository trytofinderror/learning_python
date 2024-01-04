import hashlib


class User:
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    password: str = ""
    age: int = 0

    def __init__(self, first_name: str, last_name: str, email: str, password: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.age = age

    def printAll(self) -> None:
        print(self.first_name, self.last_name, self.email, self.password, self.age)


user = User("John", "Doe", "<EMAIL>", "1qazxsw2!QAZXSW@", 18)
user.printAll()
