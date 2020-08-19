# set : 순서 x 중복 x
# set은 집합이라고도 해.

# 생성자 사용

# 다시 실행하면 순서가 바뀜. 순서가 없어서.
a = set(['1', '2', '3', '4', '4'])
print(a)

# 생성자에 iterable한 객체(sequence)를 넣으면
# iterable : ★순서대로 값을 하나씩 가지고 올 수 있도록★
# set의 값으로 각각 분리되어 들어가.
# 순서가 없고, 중복은 제거
b = set('hello')
print(b)

# {}사용 : 순서 x / 'hello'는 배열 안에 하나의 값이어서 분리가 안돼.
c = {'a', 'b', 'c', 'hello', '1', '2' ,'3'}
print(c)

c.add('World')
print(c)

# [ 합집합, 교집합 ]

# 합집합 : a와 b의 합집합 구하
print(a.union(b))
print(a | b)

# 교집합 : a와 c의 교집합 구하기
print(a.intersection(c))
print(a & c)
