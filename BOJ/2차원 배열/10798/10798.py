import sys
sys.stdin = open('input.txt')



words = []

for i in range(5):
    word = input()
    words.append(word)


result = ''
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            result += words[j][i]
print(result)