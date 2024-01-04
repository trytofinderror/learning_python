def write_to_file(filename: str, content: str) -> None:
    file = open("data/" + filename, "w")
    file.write(content)
    file.close()


def print_file_contents(filename: str) -> str:
    file = open("data/" + filename, "r");
    for line in file:
        print(line)


def get_filename() -> str:
    return input("Введите навзвание файла:")


def get_string() -> str:
    return input("Введите строку для добавления в файл:")


write_to_file(
    get_filename(),
    get_string()
)


print_file_contents(get_filename())