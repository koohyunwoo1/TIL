wool = list(map(int, input().split()))
start = list(map(int, input().split()))
wool_sum, start_sum = 0, 0
flag = False
for i in range(9):
    wool_sum += wool[i]
    if wool_sum > start_sum:
        flag = True
    start_sum += start[i]

if wool_sum < start_sum and flag == True:
    print('Yes')
else:
    print('No')