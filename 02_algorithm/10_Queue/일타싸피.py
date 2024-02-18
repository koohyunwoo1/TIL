import math

start = (1,1)
end = (2,2)

a = abs(end[0] - start[0])
b = abs(end[1] - start[1])

r = math.sqrt(a**2 + b**2)
print(r)
# 대각선의 길이

radian = math.atan(b/a)
print(r, math.degrees(radian))

# 아크탄젠트

'''
공의 직경 5.73


'''