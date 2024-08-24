# 2217 로프
n = int(input())
r_list = []

for i in range(n):
    r_list.append(int(input()))
r_list.sort()

answers = []
for x in r_list:
    answers.append(x * n)
    n -= 1
print(max(answers))