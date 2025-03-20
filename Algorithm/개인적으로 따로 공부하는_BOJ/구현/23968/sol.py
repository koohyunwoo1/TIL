import sys

# 배열 A의 크기 N, 교환 횟수 K 입력받기
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

def bubble_sort(lst, K):
    cnt = 0  # 교환 횟수 카운트

    # 버블 정렬 수행
    for i in range(len(lst), 0, -1):
        for j in range(i - 1):
            # 두 수 비교 후 정렬
            if lst[j] > lst[j + 1]:
                cnt += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                # K번째 교환이 발생하면 작은 값부터 출력
                if cnt == K:
                    print(min(lst[j], lst[j + 1]), max(lst[j], lst[j + 1]))
                    return

    # 교환 횟수가 K보다 작으면 -1 출력
    print(-1)

# 함수 실행
bubble_sort(A, K)
