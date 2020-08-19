# int() : 정수형으로 형변환 해주는 애
print(int(12.34)) # 결과값 : 12 / 실수형을 정수형으로 형변환
print(int('56')) # 결과값 : 56 / 문자를 정수형으로 형변환

print(int(True)) # 결과값 : 1 / true의 결과는 1(이상)
print(int(False)) # 결과값 : 0 / false의 결과는 0

# 2진수, 8진수, 16진수
print(int('1111', 2)) # 2진수 표현하기
print(int('77', 8)) # 8진수 표현하기
print(int('ff', 16)) # 16진수 표현하기

# float() : 실수로 형변환 해주는 애
print(float('3')) # 결과값 : 3.0
print(float(3.3)) # 결과값: 3.3 / 실수형 => 실수형이라서

#str() : 문자열로 형변환
a = 10
# print("a : " + a) # 결과값 : 에러 / 타입이 달라서.
print(" a : " + str(a)) # 문자열은 같은 Type이어야 +가 가능하다.
