    # 아래 함수를 수정하시오.
def reverse_string(word):
    word_list = list(word)
    word_list.reverse()
    word_reverse = ''.join(word_list)
    return word_reverse 


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH




# 슬라이싱

def reverse_string(word):
    return word[::-1]

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
