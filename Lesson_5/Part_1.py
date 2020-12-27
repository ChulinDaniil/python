with open("text.txt", "w", encoding="utf-8") as text_list:
    while True:
        user_string = input()
        if user_string == '':
            break
        text_list.write(user_string+'\n')
