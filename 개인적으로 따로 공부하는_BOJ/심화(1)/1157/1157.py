import sys
sys.stdin = open('input.txt')

str = input().upper()

str_set = list(set(str))
# set의 특성을 이용해서 중복제거
lst = []
for i in str_set:
    count = str.count(i)
    lst.append(count)

if lst.count(max(lst)) >= 2:
    print('?')
else:
    print(str_set[lst.index(max(lst))])