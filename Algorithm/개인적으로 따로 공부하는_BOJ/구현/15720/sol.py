import sys
input = sys.stdin.readline

# B = 버거의 개수
# C = 사이드 메뉴의 개수
# D = 음료의 개수

B, C, D = map(int, input().split())

burger_price = list(map(int, input().split()))
side_price = list(map(int, input().split()))
drink_price = list(map(int, input().split()))

burger_price.sort(reverse=True)
side_price.sort(reverse=True)
drink_price.sort(reverse=True)

result = 0
min_value = min(B,C,D)

for i in range(min_value):
    result += (burger_price[i] + side_price[i] + drink_price[i]) * 0.9

result += sum(burger_price[min_value::])
result += sum(side_price[min_value::])
result += sum(drink_price[min_value::])

print(sum(burger_price) + sum(side_price) + sum(drink_price))
print(int(result))