list = input('привет, напиши что-нибудь ').split()
print(list)

item = 0
for a in range(int(len(list) / 2)):
    list[item], list[item + 1] = list[item + 1], list[item]
    item += 2

print(list)
