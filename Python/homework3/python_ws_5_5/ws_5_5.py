def even_elements(arr):
    result = []
    tmp = []
    # 전체 리스트의 요소를 순회
    # 리스트에 값이 있는 동안 순회
    while arr:
        # 0번째 요소를 pop -> pop에 인자를 안넣으면 뒤에서부터 제거
        # -> 리스트의 순서가 바뀔 수 있음.
        element = arr.pop(0)
        # 각 요소들을 하나씩 뽑아, 짝수인 경우에만
        if element % 2 == 0:
            # 임시변수 tmp에 추가
            tmp.append(element)
    # extend는 순회 가능한 요소를 모두 순회하며 리스트에 추가하는 메서드
    result.extend(tmp)
    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)



# 아래 함수를 수정하시오.
def even_elements(my_list):
    result_list = []
    for num in my_list:
        if num % 2 == 0:
            result_list.append(num)
    return result_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
