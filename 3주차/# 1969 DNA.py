# 1969 DNA
n, m = map(int, input().split())
dna = [list(input()) for _ in range(n)]

ans1 = ''
ans2 = 0 

for i in range(m):
    nucleo = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for j in range(n):
        value = dna[j][i]
        nucleo[value] += 1 
    ans1 += max(nucleo, key=nucleo.get) 

for x in range(n):
    for y in range(m):
        if ans1[y] != dna[x][y]: 
            ans2 += 1
print(ans1)
print(ans2)
