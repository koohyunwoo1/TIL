def bubble_sort(numbers):
    # n-1 번째 까지 조사를 해나갈 것.
    # range(start, end, step)
    # -> start : 작성된 정수 부터 시작
    # -> end : 작성된 정수 - step 까지
    # -> step : 다음 정수의 값
    for i in range(len(numbers) - 1, 0, -1):
        # 이번 회차에 조사 해야 할 범위
        for j in range(i):
            # print(numbers[j], numbers[j+1])
            # j가 다음 위치 보다 값이 크면 (오름차순 기준)
            if numbers[j] > numbers[j + 1]:
                # 둘의 값을 바꿔치기 한다.
                # tmp = numbers[j]
                # numbers[j] = numbers[j+1]
                # numbers[j+1] = tmp
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                print(numbers, numbers[j], numbers[j + 1])
    return numbers


numbers = [55, 7, 78, 12, 42]

print(bubble_sort(numbers))