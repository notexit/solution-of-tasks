cmnd = input("Enter command : ").lower()

R = 0
L = 0
steps = []

s = 0
d = 0

x = 0
y = 0

sensor = "x"

walk = 0

num = "0"

if len(cmnd) <= 10000:
    for i in cmnd:
        walk = walk + 1
        try:
            if int(i) or int(i) == 0:
                num = num + i
                if len(cmnd) == walk:
                    steps.append(int(num))

        except:
            if int(num) >= 0:
                steps.append(int(num))
                if int(num) >= 100:
                    print("many steps")
                    break
                num = str()
            if str(i):
                if i == "r":
                    steps.append(i)
                    R = R + 1
                elif i == "l":
                    steps.append(i)
                    L = L + 1
                else:
                    print("I do not know such a team '{0}' ".format(i))

#вираховуємо координати
    for i in steps:
        try:
            if sensor == "x":
                if d%2 == 0:
                    y = y - i
                else:
                    x = x + i
            elif sensor == "y":
                if s%2 == 0:
                    x = x - i
                else:
                    y = y + i

        except:

            if i == "r":
                d = d + 1
                sensor = "x"
            elif i == "l":
                s = s + 1
                sensor = "y"

else:
    print("many characters")

print("""
X =     {0}
Y =     {1}
""".format(x, y))
