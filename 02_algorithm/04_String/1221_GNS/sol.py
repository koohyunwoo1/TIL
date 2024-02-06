import sys
sys.stdin = open('input.txt')

T = int(input())



arr = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
# ZRO부터 NIN 까지 문자열을 arr 리스트에 담는다.

for _ in range(1,T+1):
    num , n = input().split()
    # 테스트의 케이스 번호, 길이
    data = list(input().split())
    # 테스트케이스를 data에 넣어준다.
    for i in range(int(n)):
        data[i] = arr.index(data[i])
    # data 리스트의 각 요소를 arr 리스트의 해당 인덱스를 찾아서
    # data[i]에 갱신한다.
    data.sort()
    # data를 오름차순으로 정렬한다.
    for i in range(int(n)):
        data[i] = arr[data[i]]
    # 다시 data[i]를 인덱스로 하여 arr리스트에서 문자열을 가져와
    # data[i]에 할당한다.
    print(num)
    print(*data)