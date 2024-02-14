import sys
sys.stdin = open('input.txt')

'''
1 = 가위
2 = 바위
3 = 보
그룹은 2개로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 
최종 승자가 된다.


'''
def group(i, j):
    if i == j:     # 참가자가 한명 남았을때
        return i   # 그 한명남은 참가자를 반환한다.
    else:   # 조별로 가위바위보를 진행할때
        group_one = group(i, (i+j)// 2)
        # 왼쪽 그룹 i 부터 (i+j) //2 까지
        group_two = group((i+j)//2 + 1, j)
        # 오른쪽 그룹 (i+j)//2에서 +1 한것부터 j 까지
        return win(group_one, group_two)
    
    # group_one이 한명남았을때, 그 한명이 남게되고
    # group_two도 마찬가지이다.

def win(i, j):
    if card[i] == card[j]:
        return i
    elif card[i] == 1:
        if card[j] == 2:
            return j
        else:
            return i
    elif card[i] == 2:
        if card[j] == 1:
            return i
        else:
            return j
    elif card[i] == 3:
        if card[j] == 1:
            return j
        else:
            return i
        


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int ,input().split()))
    print(f'#{tc} {group(0, N-1) + 1 }')