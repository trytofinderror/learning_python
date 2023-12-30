def array_2_string(arr):
    string = ""

    for item in arr:
        if type(item) == list:
            string += array_2_string(item)
        else:
            string += " " + str(item)

    return string


str_list = [["some", "special"], ["text", "for", "you"], ["-", 50]]

print(
    array_2_string(
        str_list
    )
)
