n = int(input())
score = [[], [], []]
sum = []

for i in range(n):
    a, b, c = map(int, input().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)
    
for i in range(n):
    get = 0
    for j in range(3):
        if score[j].count(score[j][i]) == 1:
            get += score[j][i]
    sum.append(get)
for i in sum:
    print(i)