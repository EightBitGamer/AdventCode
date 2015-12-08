test = raw_input(">")
houses = []
pos = [0,0]

def conv(pos):
    e,n = pos
    if e >= 0:
        e = "e" + str(e)
    else:
        e = "w" +str(-e)
    if n >= 0:
        n = "n" + str(n)
    else:
        n = "s" +str(-n)
    return e+n

houses.append(conv(pos))
for d in test:
    if d == "^":
        pos[0] += 1
    elif d == "v":
        pos[0] -= 1
    elif d == ">":
        pos[1] += 1
    elif d == "<":
        pos[1] -= 1
    if conv(pos) not in houses:
        houses.append(conv(pos))

ans = 0
check = []
print len(houses)
