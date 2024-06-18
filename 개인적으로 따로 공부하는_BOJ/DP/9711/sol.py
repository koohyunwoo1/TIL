import sys
input = sys.stdin.readline

def fibonacci_modulo(n, m):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = (fib[i-1] + fib[i-2]) % m
    
    return fib[n]

T = int(input())

for i in range(1, T + 1):
    P, Q = map(int, input().split())
    result = fibonacci_modulo(P, Q)
    print(f'Case #{i}: {result}')
