# 아래 함수를 수정하시오.
def remove_duplicates(arr):
    new_list = []
    for i in arr:
        if i in new_list:
            arr.remove(i)
        else:
            new_list.append(i)
    return arr


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])  # 2 하나 4 하나 제거
print(result)
