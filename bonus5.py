waiting_list = ["sen", "ben", "jon"]
waiting_list.sort(reverse=True)

for index, item in enumerate(waiting_list):
    row =f"{index}.{item.capitalize()}"
    print (row)