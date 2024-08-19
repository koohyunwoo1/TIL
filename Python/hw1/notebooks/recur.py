# 팩토리얼
# 5! -> 5*4*3*2*1

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

def fact_while(n):
    # 최종 결과물
    result = 1
    # 종료 조건 ~동안
    while n > 1:
        result *= n
        n -= 1
    return result
print(fact_while(5))


# for 문
def fact_for(n):
    # 최종 결과물
    result = 1
    # 정해진 범위 내 순회
    for i in range(n, 0, -1):
        result *= i
    return result
print(fact_for(5))


# 피보나치
def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
print(fibo(4))