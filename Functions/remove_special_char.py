import json


def remove_special_char_from_file(input_string):
    alpha = ""
    num = ""
    special = ""
    for char in input_string:
        if char.isalpha():
            alpha += char
        elif char.isdigit():
            num += char
        else:
            special += char
    myDict = {"alpha": alpha, "num":num, "special":special}
    return json.dumps(myDict)


input_string = "ASDFGH458485425JERTYU$%^&*()"
print(remove_special_char_from_file(input_string))
