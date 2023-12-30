def list_2_string(arr: list) -> str:
    string = ""

    for item in arr:
        if type(item) is list:
            string += list_2_string(item)
        else:
            string += " " + str(item)

    return str(string)


str_list = [["some", "special"], ["text", "for", "you"], ["-", 50]]

print(
    list_2_string(
        str_list
    )
)
