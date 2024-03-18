import sys
sys.stdin = open('input.txt')

'''
B에 저장된 리스트가 A에 들어있는 수인지 확인하려고 한다.
전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m = (l+r) // 2이고,

a가 찾아야 될 숫자
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = sorted(list(map(int, input().split())))  # 정렬된 상태의 데이터
    b = list(map(int, input().split()))
    cnt = 0

    for num in b:
        start = 0
        end = N - 1
        found = 0

        while start <= end:
            mid = (start + end) // 2

            if num == a[mid]:
                cnt += 1
                break

            elif num < a[mid]:
                end = mid - 1
                if found == 1:
                    break

                found = 1

            elif num > a[mid]:
                start = mid + 1
                if found == -1:
                    break

                found = -1

    print(f'#{tc} {cnt}')


