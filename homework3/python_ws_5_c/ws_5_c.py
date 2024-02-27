def restructure_word(word, arr):
    for char in word:
        # 메서드 가 아닌 in 연산자로 확인 할 수 도 있음
        # if char in '123456789' # char 가 1~9 사이에 있다면
        # 정수인지 판별하는 메서드
        if char.isdecimal():
            # 정수로 변환 가능하므로 range로 범위 산정
            # 해당 횟수만큼 리스트의 뒤에서부터 값 제거
            for _ in range(int(char)):
                arr.pop()
        else:
            # 특정 대상 찾아서 값 제거
            arr.remove(char)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
arr = []
# list로 original_word를 형 변환 한 후, 리스트 + 리스트 할 수도 있으나,
# 형 변환 과정 거칠 필요 없이 extend 메서드로 한번에 해결
arr.extend(original_word)
print(arr)

word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
result = restructure_word(word, arr)
print(result)
print(''.join(result))

########