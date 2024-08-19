# def sum(a, b):
#     return a + b
#
# def other():
#     return sum(3, 4)
#
# # result = sum(3, 4)
# # result2 = other()
# result = other()
# print(result)
# # print(result2)


def some(n):
    if n == 0:
        return 1
    else:
        n -= 1
        print(n)
        return some(n)

result = some(10)
# result = some(0)
print(result)

# def 어떤일을하는 함수():
#     if 이조건을 만족한다면:
#         return 특정값을 반환
#     elif 만족하지 못한다면:
#         어떤 일을 수행
#         어떤일을 하는 함수()
#
#
# while 이 조건을 만족하는 동안:
#     어떤 일을 수행
#
#
#
# 어떤일을하는 함수()