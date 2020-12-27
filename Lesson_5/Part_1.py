with open("text.txt", "w", encoding="utf-8") as text_list:
    data = []
    while True:
        user_string = input()
        if user_string:
            break
        data.append(user_string)
    text_list.writelines(user_string)
