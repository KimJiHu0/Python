# -*- coding:utf-8 -*-

i = 1

while i <= 10:
    if i > 5:
        break
    print(i)
    i += 1
else:
    print('i', i,sep='=', end=' ')

# 출력예상 : 1,2,3,4,5   

print()

for i in range(1, 11):
    if i%2==0:
        continue
    print(i)
else:
    print('i', i, sep='=', end=' ')

# 출력예상 : 1,3,5,7,9 i=10