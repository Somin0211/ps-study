# 22864 피로도
A, B, C, M = map(int, input().split())

T = 0 
DW = 0

for i in range(24):
    if T > M:
        print(0)
    else:
        if T + A <= M:
            T += A
            DW += B
        else:
            if T - C >= 0:
                T -= C
            else:
                T = 0
print(DW)