#number : 숫자

# 정수형
# Python은 모든것들이 객체라 <class 'int'>라고 출력이 돼
a = 100
print(a)
print(type(a))

# 형변환 [ 실수=> 정수 ] 이 경우 <class 'int'>라고 출력이 돼.
# 문자열로 되어있던 숫자 '10'을 int로 형변환했기 때문에 int형으로 출력돼.
print(int(9.8))
print(int(7/6))
print(type(int('10')))

# 실수형
# Python은 float라는 것을 가지고 저장을 해서 형변환을 할 경우에는 float로 해야해
b = 100.1
print(b)
print(type(b))

# 형변환 [ 정수 => 실수 ] 이 경우 <class 'float'>라고 출력이 돼
# 문자열로 되어있던 '1.2'는 float로 형변환을 해주었기 때문에 float라고 출력
# Java에서는 실수형 기본이 double였는데 Python에서는 float가 기본이야.
print(float(4))
print(float(3 + 2))
print(type(float('1.2')))

#2진수(0b), 8진수(0o), 16진수(0x)
c=0b1111
print(c)

b=0o77
print(b)

e=0xff
print(e)

