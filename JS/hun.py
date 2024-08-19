N = int(input())
lst = list(map(int, input().split()))
total = int(input())
lst.sort()
# print(lst)
s = 0
e = 485
while s <= e:
    m = (s+e) / 2
    sum_num = 0
    for num in lst:
        sum_num += num
        if sum_num >= total:
            e = (m+e)/2
            break
        else:
            m =