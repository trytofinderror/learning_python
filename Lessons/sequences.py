my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]  # список имеет все свойства обычного нумерованного массива
print(my_list)

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # кортеж неизменяем, данные можно только выводить
print(my_tuple)

mnz = set(my_list)  # множество - автоматически сортируется в случайном порядке, внутри себя имеет только уникальные значения, в остальном имеет все свойства нумерованного массива
print(mnz)

frz = frozenset(my_list)  # неизменяемое множество, обладает всеми свойствами множества, но неизменяемо
print(frz)

my_dict = {
    "name": "Vasya",
    "age": 21,
    "country": "Norway"
}  # словарь (обладает всеми свойствами ассоциативного массива)

print(
    my_list.pop(4)  # pop возвращает значение удаленного элемента, remove не возвращает ничего
)
