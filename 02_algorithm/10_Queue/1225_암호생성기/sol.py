import sys
sys.stdin = open('input.txt')


'''
1~5까지 감소하는 사이클이 있음
숫자가 감소할때 0보다 작아지는 경우 0으로 유지됨.

제약사항 
마지막 암호 배열은 모두 한 자리 수로 구성되어있음.

'''

for tc in range(1, 11):
    T = int(input())
    num = list(map(int, input().split()))


    while num[-1] > 0:
        for i in range(1, 6):
            new_num = num[0] - i
            if new_num <= 0:
                new_num = 0
            num.pop(0)
            num.append(new_num)
            if num[-1] == 0:
                break

    print(f'#{tc} {" ".join(map(str, num))}')


