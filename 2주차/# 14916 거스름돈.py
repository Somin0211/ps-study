# 14916 거스름돈
x = int(input())

count = 0
i = 0
while True:
    if x % 5 == 0:  
        count += x // 5
        break
    else:
        x -= 2  
        count += 1

    if x < 0:  
        break
if x < 0:	
    print(-1)			
else:
    print(count)