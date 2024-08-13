# 10989 수 정렬하기 3
import sys

def input():
    return sys.stdin.readline()

n = int(input())    ### 코랩에서는 왜 오류나는지 모르겠음
count = [0] * 10001

for _ in range(n):
    num = int(input())
    count[num] += 1
for i in range(1, 10001):
    if count[i] > 0:
        sys.stdout.write((str(i) + '\n') * count[i])
