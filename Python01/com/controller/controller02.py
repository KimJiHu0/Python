# -*- coding:utf-8 -*-

# 반복문

subject = ['java', 'javascript', 'python']

# subject의 하나하나를 가져와서 i에 담을거야.
for i in subject:
    print(i, end=' ')
else: # 해당 반복문이 완벽하게 다 종료되었을 때 else구문이 실행 돼.
    print('재밌다.')

for i in range(1, 100): # 1부터 100-1 까지
    print(i, end='+')
    
# 구구단  해보자!
print('\n구구단!')
for i in range(2, 10):
    print('<<'+str(i)+'단>>>')
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, i*j))
        
# reverse
for i in range(1, 11):
    print(i, end=' ')
print()
for i in range(10, 0, -1): # 10부터 0까지 -1씩 증가할거야~
    print(i, end=' ')
