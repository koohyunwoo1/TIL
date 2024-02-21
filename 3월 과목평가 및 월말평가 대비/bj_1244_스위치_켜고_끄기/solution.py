import sys
sys.stdin = open('input.txt')
'''
남학생 -> 스위치번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
여학생 -> 자기가 받은 수의 스위치를 중심으로 좌우대칭이면서 가장 많은 스위치를 포함
하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
'''
'''


'''

switch_num = int(input())  # 스위치의 개수
switch = list(map(int, input().split()))  # 스위치의 현재 상태
student = int(input())  # 학생 수 

for st in range(student):
    gender , number = map(int, input().split())  # 한 학생의 성별, 학생이 받은 수
    
    # 남자인 경우
    if gender == 1:
        for i in range(number, switch+1, number):
            # if switch[i] == 0:
            #     switch[i] = 1
            switch[i] = 1 - switch[i]
            # else:
            #     switch[i] = 0

    # 여자인 경우
    else:
        if switch[number] == 0:
            switch[number] = 1
        else:
            pass


