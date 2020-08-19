# tuple : list와 거의 같아.

# 생성자 사용
a = tuple()
print(a)

# 'tuple' object has no attribute 'append' : append라는 속성이 없어.
# 추가 수정 삭제할 수 없어.
#a.append(1)
#print(a)

# tuple생성자는 한개의 값만 들어가야하는데 4개의 값이 들어가서 안돼. 
#b = tuple(1,2,3,4)
#print(b)

b = tuple([1,2,3,4])
print(b)
list_b = list(b)
print(list_b)
list_b.append(5)
print(list_b)

# () 사용
c = (1,2,'3')
print(c)

# tuple + tuple
d = b + c
print(d)

#unpacking : 얘는 하나하나 값을 넣어준대!
e = (1,2,3,4)
f,g,h,i = e
print(f)
print(g)
print(h)
print(i)

