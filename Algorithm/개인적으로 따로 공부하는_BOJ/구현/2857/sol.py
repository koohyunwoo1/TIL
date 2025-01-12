result = []
for i in range(1,6):
    S = input()
    if "FBI" in S:
        result.append(i)
if len(result) == 0:
    print("HE GOT AWAY!")
else:
    print(*result)