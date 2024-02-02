#  bubble sort

# def bubble_sort(arr, arr_len):
#     for i in range(arr_len - 1 , 0, -1):
#         for j in range(0, i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1] , arr[j]
    
#     return arr

# list = [5,5,4,1,6,9,5,1,1,5,3,5,8,7,3]
# list_len = len(list)

# print(list)
# result = bubble_sort(list, list_len)
# print(result)   # bubble sort 오름차순으로 정렬됨.

def bubble_sort_revers(arr, arr_len):
    for i in range(arr_len-1, 0 , -1):
        for j in range(0, i):
            if arr[j] < arr[j+1]:   # 내림차순
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    return arr

list = [5,5,4,1,6,9,5,1,1,5,3,5,8,7,3]
list_len = len(list)

print(list)
result = bubble_sort_revers(list, list_len)
print(result)   # bubble sort 내림차순으로 정렬됨.



# counting sort