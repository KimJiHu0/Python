# -*- coding:utf-8 -*-

# [] list / {} set, dictionary / () tuple


# Split : 문자열 자르기
str01 = 'Hello, World!\nHello, Python'
print(str01)

arr01 = str01.split(' ') # 공백으로 자르자는 의미
print(arr01) # ['Hello,', 'World!\nHello,', 'Python']로 출력되는데 list로 return

arr02 = str01.split(' ', 1) # 공백으로 자르긴 할건데 1개로 잘라줘.
print(arr02)


import re
arr03 = re.split("[\s]|[,]",str01)
print(arr03)

# Join (Join함수는 굉장히 자주 사용돼.)

arr04  = ['1', '2', '3', '4']
print(arr04)
a = '+'.join(arr04) # '+'라는 문자열이 arr04의 배열 사이사이에 추가되었다.
print(a)

# eval : 문자열로 만들어진 연산처리
print(eval(a))
