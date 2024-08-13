# 1181 단어 정렬
x = int(input())
words = []

for i in range(x):
    words.append(input())

words = list(set(words))
words.sort()
words.sort(key = len)

for i in words:
    print(i)