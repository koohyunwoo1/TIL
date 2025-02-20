n = int(input())
if n > 1:
    print("int a;")
    print("int *ptr = &a;")
    print("int **ptr2 = &ptr;")
    for i in range(3,n+1):  
        print("int "+"*"*i+"ptr"+str(i)+" = &ptr"+str(i-1)+";") 
else:
    print("int a;")
    print("int *ptr = &a;")