# list
# 순서가 있고, 중복이 가능하다

# 생성자 사용
a = list()
print(a)
a.append(1)
print(a)
a.append('a')
print(a)
a[0] = 3
print(a)
# 아래의 경우 list assignment index out of range가 뜬다.
# 리스트가 자동으로 크기가 커지긴 하는데 해당 index로 값을 추가하는건 안돼.
#a[2] = 5
#print(a)
a.append(3)
print(a)

# [] 사용
b = [1,2,3,4,5]
print(b)

# b 안에 있는 숫자2와 4를 더해서 출력
one = b[1] # b에 1번지 숫자 one에 담기
two = b[3] # b에 3번지 숫자 two에 담
print(one + two)

# reverse(거꾸로)
b.reverse()
print(b)

# sort (정렬)
b.sort()
print(b)

c = ['a', 'b', 'c', 'd', ['e', 'f', 'g'], 'h']
print(c[4])

d = b + c
print(d)

print(c + d)
