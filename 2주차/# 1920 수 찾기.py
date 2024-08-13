# 1920 수 찾기
import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for m in m_list:
    result = False
    for n in n_list:
        if m == n:
            print(1)
            result = True
            break

    if result == False:
        print(0)