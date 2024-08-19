import sys
input = sys.stdin.readline

def min_max_replace(a, b):
    min_a = int(a.replace('6', '5'))
    min_b = int(b.replace('6', '5'))
    min_sum = min_a + min_b
    
    max_a = int(a.replace('5', '6'))
    max_b = int(b.replace('5', '6'))
    max_sum = max_a + max_b
    
    return min_sum, max_sum

a, b = input().split()

min_value, max_value = min_max_replace(a, b)

print(min_value, max_value)
