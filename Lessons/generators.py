
#yield - используется для возврата значения функции с сохранением состояния локальных переменных функции

def generator(i: int) -> int:
    while i > 0:
        yield i
        i -= 1


g = generator(6)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

