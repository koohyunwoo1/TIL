A = list(map(int, input()))
B = list(map(int, input()))
arr = [0]*16
for i in range(16):
    if i % 2 == 0:
        arr[i] = A[i//2]
    else:
        arr[i] = B[i//2]

#print(arr)

while len(arr) != 2:
    temp = []
    for i in range(len(arr)-1):
        num = (arr[i]+arr[i+1]) % 10
        temp.append(num)
    arr = temp

print(*arr, sep="")
