import sys
input = sys.stdin.readline

if __name__ == '__main__':
    ms = input()
    n = int(input())
    w_list = sorted([input() for i in range(n)])

    max_p = max_i = 0
    for i in range(n):
        L = ms.count('L') + w_list[i].count('L')
        O = ms.count('O') + w_list[i].count('O')
        V = ms.count('V') + w_list[i].count('V')
        E = ms.count('E') + w_list[i].count('E')
        p = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
        if p > max_p:
            max_p = p
            max_i = i
    print(w_list[max_i])