# 주어진 문자열에서 특정 문자의 개수를 세는 count_character 함수를 작성하시오.
# 문자열과 대상 문자를 인자로 받아 개수를 반환해야한다.
# 아래 함수를 수정하시오.
# def count_character(word, char):
#    return word.count(char)


###################### 반복분
def count_character(word, char):
   result = 0 # 해당하는 알파벳이 나올때마다 1씩 증가
   # 전체 순회
   for text in word:
      # print(text)
      # 순회해서 얻은 text 변수에 든 값이
      # char 매개변수에 들어있는 값과 일치 하다면
      if text == char:
         result += 1
   # 전체 순회를 완료 했다 -> 모든 상황에 대한 조사가 끝났다.
   return result

result = count_character("Hello, World!", "o")
print(result)  # 2         # 인자 1      # 인자2
######################### 반복문