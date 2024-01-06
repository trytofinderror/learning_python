import pickle


def serialize(data, filename: str = "data/user.pickle") -> None:
    file = open(filename, "wb")
    pickle.dump(data, file)
    file.close()


def deserialize(filename: str = "data/user.pickle") -> str:
    file = open(filename, "rb")
    data = pickle.load(file)
    file.close()
    return data


user = {'username': 'John', 'password': '<PASSWORD>', 'age': 34, 'weight': 87}
serialize(user, "data/user.pickle")

print(
    deserialize("data/user.pickle")
)
