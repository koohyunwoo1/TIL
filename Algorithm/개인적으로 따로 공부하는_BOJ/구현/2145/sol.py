while(True):
    n = int(input())
    if n == 0:
        break
    while(n>9):
        n = sum(map(int,list(str(n))))
        # n이 673일 때, 스트링 변환 후 리스트에 담으면 ["6","7","3"] 꼴이 된다.
        # map은 이같은 배열 안의 스트링을 int형으로 편하게 변환시켜 주는 기능을 한다.
    print(n)