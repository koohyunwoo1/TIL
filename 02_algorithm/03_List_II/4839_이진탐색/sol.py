import sys
sys.stdin = open('input.txt')

    # 내가 찾고하는 값 이  7이다
    # 중앙 값 5를 찍고
    # 정렬되어 있는것은 알지만
    # 오름차순인지 내림차순인지 모름


    # 문제 
    # 책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 떄 , 이진탐색에서 이긴 사람이 누구인가 ?
    # 비긴 경우는 0

    # 전체 쪽수, 찾을 쪽 번호
def binarySearch(page, target): 
    # binarySearch 함수를 만들어줌.
    # page : 전체 쪽 수
    # target : 찾을 쪽 번호
    left = 1
    # left : 첫 페이지
    right = page
    # right : page로 할당해서 전체 쪽 수
    count = 0
    # count 
    while left <= right:
        mid = (left + right) // 2
        # mid 값에 첫페이지와 전체 쪽 수를 2로 나눈 값
        if mid == target:
            # mid의 값과 찾을 쪽 수가 같다면 
            return count
            # count를 반환해준다.
        elif mid < target:
            # mid의 값이 target의 값보다 작다면
            left = mid
            # left의 값이 mid의 값이 된다.
            count += 1
            # count는 1 증가
        elif mid > target:
            right = mid
            count += 1

T = int(input())       
# 테스트 케이스 
for _ in range(1, T+1):
    # 테스트 케이스 수 만큼 반복해준다.
    page, A, B = map(int, input().split())
    # 전체 쪽수, A,B가 찾을 쪽 번호
    count_A = binarySearch(page, A)
    count_B = binarySearch(page, B)
    
    if count_A < count_B:
        # A가 B보다 먼저 찾았다면 
        print(f'#{_} A')
        # A 출력
    elif count_A > count_B:
        # B가 A보다 먼저 찾았다면
        print(f'#{_} B')
        # B 출력
    else:
        # 동시에 찾았다면 0을 출력
        print(f'#{_} 0')


    

