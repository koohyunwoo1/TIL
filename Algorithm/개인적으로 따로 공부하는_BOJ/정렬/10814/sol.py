import sys
sys.stdin = open('input.txt')

# 현재 데이터가 가입한 순서되로 되어있음.
# 나이 순으로 정렬하는데 , 나이가 같으면 가입된순으로 정렬해라.
N = int(input())

arr = []
for tc in range(N):
    age, name = map(str, input().split())
    age = int(age)
    arr.append([age, name])

for i in sorted(arr, key=lambda  x : x[0]):
    print(i[0], i[1])


