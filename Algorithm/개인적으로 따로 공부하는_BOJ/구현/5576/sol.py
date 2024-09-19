import sys
input = sys.stdin.readline

w_points = []
k_points = []
for i in range(10):
    w_points.append(int(input()))
for i in range(10):
    k_points.append(int(input()))
w_points.sort(reverse=True)
k_points.sort(reverse=True)
print(sum(w_points[:3]), sum(k_points[:3]))