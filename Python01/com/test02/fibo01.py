# -*- coding:utf-8 -*-


# fibonacci 수열
# 0 1 1 2 3 5 8 13 21 34 55 ... 앞에 숫자와 뒤에숫자를 더해서 나온 값을 출력해주는거

n = input('input n : ') # java의 scanner과 동일해.
a, b = 0, 1
i = 0
while i < int(n):
    print(a, end=' ')
    a, b = b, a+b   # 0과 1에서 1과 1로 넘어가겠다. 즉, 옆으로 한칸 이동하겠다.
    i += 1