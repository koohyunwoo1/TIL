import sys
sys.stdin = open('sample_input.txt')

# # 0~9까지 숫자가 적힌 N장의 카드가 주어진다.
# # 가장 많은카드에 적힌 숫자와 카드가 몇장인지 출력하는 프로그램을 만드시오.
T = int(input())

for i in range(1, T+1):
    N = int(input())  # 카드 장수
    a = list(map(int, input()))  # 카드에 적힌 숫자
    a.sort(reverse=True)  # 내림차순으로 정렬해주자.
    max_a = max(a, key = a.count)  # a중 최빈값 구하자      
    count_a = a.count(max_a)   # 몇개가 가장 최빈값인지 알아보자.
    print(f'#{i} {max_a} {count_a}')




# # 강사님 풀이
# T = int(input())


# for tc in range(1, T+1):
#     N = int(input())

#     ai = list(map(int,input()))
#     print(ai)

#     counting_list = [0 for _ in range(10)]

#     for num in ai:
#         counting_list[num] += 1

#     max_count = 0
#     result = 0

#     for i in range(10):

#         if max_count <= counting_list[i]:
#             max_count = counting_list[i]
#             result = i

#         print(f'#{i} {result}')