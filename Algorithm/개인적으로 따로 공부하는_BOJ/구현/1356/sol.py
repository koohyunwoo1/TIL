N = input()
ok = 0
for i in range(1, len(N)):
    s1, s2 = N[:i], N[i:]
    m1 = m2 = 1
    for n in s1:
        m1 *= int(n)
    for n in s2:
        m2 *= int(n)
    if m1 == m2:
        ok = 1
        break
print("YES" if ok else "NO")