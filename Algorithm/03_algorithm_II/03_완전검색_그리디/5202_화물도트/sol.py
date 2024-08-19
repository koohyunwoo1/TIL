import sys
sys.stdin = open('input.txt')

'''
최대 몇 대의 화물차가 이용할 수 있는지 ?
작업 시작 시간과 완료시간이 매시 정각을 기준으로 표시되어있고,
앞 작업의 종료와 동시에 다음 작업을 진행할수있음

'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int ,input().split())) for _ in range(N)]
    arr.sort(key=lambda  x: -x[1], reverse = False)
    # 두번째의 값으로 내림차순으로 정렬

    time = arr.pop()[1]
    # 끝나는 시간이 time에 들어있음
    result = 1
    # 최초 작업을 수행하는 화물차를 포함하기 때문에 1로 설정해준당
    while arr:
        start, end = arr.pop()

        if time <= start:   # 끝나는시간이 시작시간보다 작으면
            time = end    # time을 현재 일정의 끝나는 시간으로 업데이트하고
            result += 1   # result를 1 더해줌



    print(f'#{tc} {result}')




