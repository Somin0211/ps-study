# 27160 할리갈리
card = int(input())
card_dict = { 'STRAWBERRY' : 0, 'BANANA' : 0, 'LIME' : 0, 'PLUM' : 0}

for i in range(card):
  fruit, x = input().split()
  card_dict[fruit] += int(x)

if 5 in card_dict.values():
  print('YES')
else:
  print('NO')