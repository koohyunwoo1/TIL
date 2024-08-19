import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())

c1 = {'0': '0000' ,
     '1': '0001' ,
     '2': '0010' ,
     '3': '0011' ,
     '4': '0100' ,
     '5': '0101' ,
     '6': '0110' ,
     '7': '0111' ,
     '8': '1000' ,
     '9': '1001' ,
     'A': '1010' ,
     'B': '1011' ,
     'C': '1100' ,
     'D': '1101' ,
     'E': '1110' ,
     'F': '1111' }

c2 = {'0000': '0' ,
     '0001': '1' ,
     '0010': '2' ,
     '0011': '3' ,
     '0100': '4' ,
     '0101': '5' ,
     '0110': '6' ,
     '0111': '7' ,
     '1000': '8' ,
     '1001': '9' ,
     '1010': 'A' ,
     '1011': 'B' ,
     '1100': 'C' ,
     '1101': 'D' ,
     '1110': 'E' ,
     '1111': 'F' }

for tc in range(1, T+1):
    N, number = input().split()
    N = int(N)

    result = ''


    if N == 24:
        i = 0
        while i < len(number):
            num = number[i:i+4]
            if num in c2:
                result += c2[num]
            i += 4

    elif N == 6:
        for n in number:
            if n in c1:
                n = c1[n]
            result += n

    print(f'#{tc} {result}')




