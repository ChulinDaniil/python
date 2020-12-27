x = input('привет, напиши что-нибудь ').split()
print(x)

y = 0
for z in range(int(len(x) / 2)):
    x[y], x[y + 1] = x[y + 1], x[y]
    y = y + 2

print(z)
