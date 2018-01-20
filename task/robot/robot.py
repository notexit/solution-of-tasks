cmnd = input("Enter command : ").lower()

R = 0
L = 0
steps = []

walk = 0

num = str()

if len(cmnd) <= 10000: #перевіряємо кількість символів
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
                    R = R + 1
                elif i == "l":
                    L = L + 1
                else:
                    print("I do not know such a team '{0}' ".format(i))
else:
    print("many characters")

print("""
R =     {0}
L =     {1}
Steps = {2}
""".format(R, L, sum(steps)))
