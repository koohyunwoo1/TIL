import sys
sys.stdin = open('input.txt')

hex_to_bin = {hex(idx)[2:].upper(): f'{idx:04b}' for idx in range(16)}

T = int(input())
for tc in range(1, T+1):
    N, N16 = input().split()
    print(f'#{tc}', end=' ')
    for char in N16:
        print(hex_to_bin[char], end='')
    print()