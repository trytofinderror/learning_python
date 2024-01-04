from typing import Callable


def print_wrapper(func: Callable) -> Callable:  # враппер, оборачивает функцию другой функцией
    def wrapper():
        print("this code run before func")
        func()
        print("this code run after func")

    return wrapper


@print_wrapper  # декларация враппера перед функцией, к которой его надо применить
def print_string() -> None:
    print("string")


print_string()
