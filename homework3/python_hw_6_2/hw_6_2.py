# 아래 함수를 수정하시오.
def remove_duplicates_to_set(i):
    return set(i)   # set으로 형이 바뀌면 중복이 되지 않기 때문에 됨.

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

# 중복이 제거된 거
# 가정 : i에 1~9까지의 정수만 요소로 삽입된다면,
def remove_duplicates_to_set(i):
    count_dict = {k : 0 for k in range(1,10)}
    for num in i:
        count_dict[num] += 1
    # 모든 출현횟수 기록해둔 dict를 순회해서 
        # value가 1인 (1번 이상 나온 값) 값만 모아서 새 list
    result = [key for key, item in count_dict.items() if item >= 1]
    return set(result)
    # dict_comprehension



result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)


# 리스트로 만들어서
def remove_duplicates_to_set(arr):
    count_list = [0 for i in range(10)]
    for index in arr:
        count_list[index] += 1
    result = [num for num in range(len(count_list)) if count_list[num] >= 1]
    return result

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)




# 딕셔너리에 집중
def remove_duplicates_to_set(arr):
    # 최종 결과물
    result = set()
    duplicates_check_dict = {}
    for num in arr:
        # # 해당하는 키가 dict에 없다면
        # if dict.get(key) == None:
        #     dict[key] = 0
        # else:
        #     dict[key] += 1
        # if dict[key]: (키가 없는경우 KeyError)
        duplicates_check_dict[num] = duplicates_check_dict.get(num, 0) + 1
        # 중복없음 == 1번만 나왔으면 아무튼 나온거임
        if duplicates_check_dict[num] == 1:
            result.add(num)
    return result


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)