def counting_sort(input_arr, k):
    """
    input_arr : 입력 배열(1 to k)
    counting_arr : 카운트 배열
    k는 데이터의 개수가 아닌 데이터 원소의 범위
    """

    counting_arr = [0] * (k + 1)

    # 1. counting array에 arr내 원소의 빈도수 담기
    for i in range(0, len(input_arr)):
        counting_arr[input_arr[i]] += 1
    # for i in input_arr:
    #     counting_arr[i] += 1

    # 2. 누적(counting_arr 업데이트)
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]

    # 3. result_arr 생성
    result_arr = [-1] * len(input_arr)

    # 4. result_arr에 정렬하기(counting_arr를 참조)
    for i in range(len(result_arr) - 1, -1, -1):
        counting_arr[input_arr[i]] -= 1
        result_arr[counting_arr[input_arr[i]]] = input_arr[i]
    # for i in input_arr:
    #     counting_arr[i] -= 1
    #     result_arr[counting_arr[i]] = i

    return result_arr


a = [0, 4, 1, 3, 1, 2, 4, 1]

print(counting_sort(a, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]