import sys
sys.stdin = open('input.txt')

# N은 2 X 3 X 5 X 7 X 11
T = int(input())

for i in range(1,T+1):
    number = int(input())
    a = b = c = d = e = 0
    while number != 1:
        if number % 2 == 0:
            a += 1
            number = number / 2
        if number % 3 == 0:
            b += 1
            number = number / 3
        if number % 5 == 0:
            c += 1
            number = number / 5
        if number % 7 == 0:
            d += 1
            number = number / 7
        if number % 11 == 0:
            e += 1
            number = number / 11 

    print(f'#{i} {" ".join(map(str, (a, b ,c ,d ,e)))}')