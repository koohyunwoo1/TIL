import sys
input = sys.stdin.readline

while True: 
    n = int(input().strip())  # 입력받을 때 공백 제거
    if n == 0:
        break
 
    arr = []
 
    for _ in range(n):
        word = input().strip()  # 각 단어의 줄바꿈 문자를 제거
        arr.append(word)
 
    arr.sort(key=str.lower)  # 소문자 기준으로 정렬
    print(arr[0])  # 첫 번째 단어 출력
