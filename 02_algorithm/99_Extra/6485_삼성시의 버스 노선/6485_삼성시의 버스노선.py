import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_routes = []
    for _ in range(N):
        A, B = map(int, input().split())
        bus_routes.append((A, B))
    
    P = int(input())
    bus_stops = [list(map(int, input().split())) for _ in range(P)]

    result = []
    for stop in bus_stops:
        count = 0  # count 0으로 초기화 시켜줌
        for st in stop:
            for route in bus_routes:
                if route[0] <= st <= route[1]:
                    count += 1
        result.append(count)

print(f"#{tc} {' '.join(map(str, result))}")


