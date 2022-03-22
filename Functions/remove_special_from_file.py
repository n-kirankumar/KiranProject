import json


def remove_special_char_from_file(input_path):
    special = ""
    special_count = 0
    fileObj= open(input_path, mode ="r")
    file_string = fileObj.read()
    print(file_string)
    new_string = [i.rstrip('\n') for i in file_string]
    fileObj.close()
    for char in new_string:
        if not char.isalnum():
            special += char
            special_count += 1
    myDict = {"special_count": special_count, "special": special}
    return json.dumps(myDict)


input_path = r"D:\Python\Day 17\abc.txt"
print(remove_special_char_from_file(input_path))
