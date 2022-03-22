import json


def remove_special_char_from_file(input_string):
    alpha = ""
    num = ""
    special = ""
    special_count = 0
    for char in input_string:
        if char.isalpha():
            pass
        elif char.isdigit():
            pass
        else:
            special += char
            special_count += 1
    myDict = {"special_count": special_count, "special":special}
    return json.dumps(myDict)


input_string = "ASDFGH458485425JERTYU$%^&*()"
print(remove_special_char_from_file(input_string))
