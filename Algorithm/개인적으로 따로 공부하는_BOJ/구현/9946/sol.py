i = 1
 
while True:
    a = input()
    b = input()
    if a == "END" and b == "END":
        break
    else:
        A = sorted(list(a))
        B = sorted(list(b))
        if A == B:
            print("Case", str(i)+ ": same")
        elif A != B:
            print("Case", str(i)+ ": different")
            
        i += 1	