def d(n):
    num = list(str(n))
    asw = n
    for i in range(len(num)):
        asw += int(num[i])
    return asw

SET = list(range(1,10001))
for n in range(1,10001):
    if d(n) in SET:
        SET.remove(d(n))
    
for i in range(len(SET)):
    print(SET[i])