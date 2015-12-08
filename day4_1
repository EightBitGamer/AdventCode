import md5
m = md5.new()

key = raw_input(">")
cfor = "00000"
ans = ""
cur = 0
while ans == "":
    m = md5.new()
    m.update(key + str(cur))
    res = str(m.hexdigest())
    if res.startswith(cfor):
        ans = cur
    cur += 1
print ans
