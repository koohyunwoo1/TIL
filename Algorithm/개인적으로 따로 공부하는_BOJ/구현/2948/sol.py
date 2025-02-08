import sys
input=sys.stdin.readline

d,m=map(int,input().split())
months=[31,28,31,30,31,30,31,31,30,31,30,31]
# 1월 1일의 요일이 0번째
days=["Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday","Wednesday"]
total_day=0
for i in range(m-1):
    total_day+=months[i] # 입력된 달의 전 달까지의 일수를 더한다

total_day+=d-1 # 일수를 더한다
print(days[total_day%7])