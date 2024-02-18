import sys
sys.stdin = open('input.txt')
# 마지막까지 남아있는 피자의 번호를 알아야함
# 인덱스로 해야 할듯 ?
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))  # 치즈의 양

    pizza_number = []
    for i in range(M):
        pizza_number.append([i+1, Ci[i]])

    place_in = pizza_number[:N]  # 화덕에 현재 들어가 있는 피자
    place_out = pizza_number[N:]  # 화덕에 들어가 있지 않는 피자


    while len(place_in) != 1: # 화덕안에 피자가 하나 남을때까지 한다.
        index, pizza = place_in.pop(0)
        pizza //= 2

        if pizza != 0:   # 화덕안에 피자가 0이 아니라면
            place_in.append([index, pizza])  # 다시 화덕에 넣어준다
        elif place_out:    # 화덕에 들어가 있지 않은 피자가 비어있지 않으면
            place_in.append(place_out.pop(0))   # 화덕에 넣어준다

    print(f'#{tc} {place_in[0][0]}')