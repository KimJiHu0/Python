# -*- coding:utf-8 -*-

# 산술연산
a = 21
b = 2
print(a + b) # 23
print(a - b) # 19
print(a * b) # 42
print(a ** b) # 441 / a의 b승 => a의 b제곱
print(a / b) # 10.5
print(a // b) # 10 / 나누고 나머지 제거. => 몫(floor division)
print(a % b) # 1 / 나머지 (modulo)

print('-------')

# 비교 연산
a, b = 3, 5 # a = 3 / b = 5
print(a == b) # false
print(a != b) # true
print(a > b) # false
print(a <= b) # true
print(a is b) # false
print(a is not b) #true

print('-------')

print(True or False) # True
print(False and True) # Flase
print(not False) # True

print('-------')

# 범위연산
lst = list(range(100)) # range : 0부터 99까지 / 시작부터 끝-1까지
print(lst) # 배열에 0부터 마지막숫자-1
print(lst[2]) # 2
print(lst[12:49]) # 12 ~ 48까지만 출력 / [start : end] => [start : end-1]
print(lst[12:49: 3]) # [start : end : step] => start ~ end-1 까지 step만큼씩 출력

print('-------')

str01 = 'Hello World!'
print(str01)
print(str01[0]) # 문자열에서 index를 찍어주면 출력이 된다. 문자열이 문자 값을의 list이야.[순서가 있는 값]
print(str01[0:5]) # Hello만 출력하기.
print(str01[6:11]) # World만 출력하기. / 느낌표 전까지
print(str01[0:4]*4) #Hell 이 4번 출력된다.

print('-------')

# reverse
print(str01[-1]) # 마지막 글자 출력.
print(str01[-1:]) # -1자리부터 뒤에 끝까지.
print(str01[: -1]) # 처음부터 -1번지까지. [start : end-1] 이니까 느낌표 빼고 다 나와.
print(str01[:: -1]) # step이 -1이라는 의미ㅏ. / 처음부터 끝까지 -1씩 증가해라.(거꾸로 출력)

# 멤버연산 : 있는지 없는지 확인
lst02 = [0, 1, 2, 3, 4, 5]
print(3 in lst02) # 3은 lst02에 있니?? => True
print(5 not in lst02) # 5가 lst02에 없니?? => 있으니까 False
print(7 not in lst02) # 7이 lst02에 없니?? => 없으니까 True



