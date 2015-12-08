test = raw_input(">")
houses = []
pos = [0,0]
posr = [0,0]

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
a = True
cpos = []
for d in test:
    if a:
        a = False
        cpos = pos
    else:
        cpos = posr
        a = True
    if d == "^":
        cpos[0] += 1
    elif d == "v":
        cpos[0] -= 1
    elif d == ">":
        cpos[1] += 1
    elif d == "<":
        cpos[1] -= 1
    if conv(cpos) not in houses:
        houses.append(conv(cpos))

ans = 0
check = []
print len(houses)
