import sys
input = sys.stdin.readline

d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

max = max(d.values())
ans = []
for k, v in d.items():
    if v == max:
        ans.append(k)

ans.sort()
print(ans[0])
