import sys
sys.stdin = open('input.txt')

# 전공평점이 3.3 이상이며, 졸업고시를 통과해야한다.
# 전공평점을 계산해보자 
# 학점 x 과목평점의 합을 학점의 총합으로 나눈 값


credit = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

sum1 = 0
sum2 = 0
T = 20
for tc in range(1, T+1):
    sub, gra, rat = input().split()
    gra = float(gra)
    if rat != 'P':
        sum1 += gra
        sum2 += gra * credit[rat]

print(sum2 / sum1) 