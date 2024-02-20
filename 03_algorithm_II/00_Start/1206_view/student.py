import sys

sys.stdin = open('input.txt')

# 정해진 테스트케이스 수 10개에 대해서 반복
for i in range(1, 11):

    # 건물의 개수 N과 N개의 건물의 높이 입력값 받기
    N = int(input())
    heights = list(map(int, input().split()))

    # 최종 결과로 출력할 조망권이 확보된 세대의 수 변수 설정
    count = 0

    # 양측의 항상 높이가 0인 네칸을 제외하고 모든 건물에 대해
    for n in range(2, N - 2):

        # 해당 건물의 좌우 각각 두칸에 해당하는 건물과 비교해야 하므로
        # 슬라이싱을 통해 필요한 정보만 담은 리스트 슬라이싱
        n_list = heights[n - 2: n + 3]

        # 만약 해당 건물이 좌우 각각 두칸씩의 건물들보다 높은 것이 맞다면
        # 해당 건물을 제외하고 가장 높은 건물의 높이와의 차이를 구해
        # 조망권이 확보된 세대의 수에 반영
        if n_list[2] == max(n_list):
            now = n_list.pop(2)
            count += (now - max(n_list))

    # 최종값 출력
    print(f'#{i} {count}')