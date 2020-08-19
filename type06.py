# dictionary : == Map과 동일 순서 x , 중복 o, key x, value o
# 출력되는 형태는 JAVA의 JSON과 동일하게 나온다.
# {K : V}

# 생성자 사용
dict01 = dict()
dict01[1] = 'one'
dict01['two'] = 2
print(dict01)

# {} 사용
dict02 = {}
dict02['one'] = 1
dict02[2] = 'two'
dict02[3] = 3
print(dict02)

# key를 통해서 value값 가져오기
print(dict01.get(1))
print(dict02['one'])

# key들만 가져오기
print(dict02.keys())

# value들만 가져오기
print(dict02.values())

# 'one'이라는 key 하나만 가져오기.
# type을 찍어보면 어떤 type인지 나오니까 거기서 list면 값을 뽑아다가 출력하자.
print(type(dict02.keys()))
print(list(dict02.keys())[0])
