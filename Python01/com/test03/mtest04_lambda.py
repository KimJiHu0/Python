# -*- coding:utf-8 -*-



#lambda : 익명함수 => 함수를 만들지 않고, 선언만 해두고, 필요할때 바디를 만들어서 사용해
# java, js 는 () -> {}를 많이씀

# hap01에 lambda를 써줄건데 파라미터로 a, b를 받을거고 이를 받아서 a+b를 해준 결과값을 줄거야.
hap01 = lambda a, b:a+b
print(hap01(10,20))

gob = lambda a, b : a * b
print(gob(30, 40))

# 얘는 파라미터 1개,2개가 아니라 많이 받을 수 있어.
hap02 = lambda a,b,c, : a+b+c
print(hap02(5,6,7))

a = [(1, 'one', 9), (2, 'two', 8), (3, 'three', 7), (4, 'four', 6)]
# 위의 a는 list안에 tuple가 4개 들어가있는거야.
print(a)
a.sort(key=lambda a:a[1])
# tuple하나하나 넘어온 a값. 그 중에서 1번지에 있는 애 기준으로 sort
print(a)


min01 = (lambda x, y :x if x < y else y)(11,22)
# lambda에 x와y를 받을건데 / 만약에 x가 y보다 작다면 x를 return , 아니면 y를 return
print(min01)


# lambda에 x와y를 파라미터로 받을건데 만약에 x가 y보다 크면 x를 return하고 아니면 y를 return해.
max01 = (lambda x,y : x if x > y else y)(10,5)
print(max01)

b = lambda x : (lambda y : x + y)
c = b(100) # lambda y : 100 + y
d = c(90) # 100 + 90
print(d)
print(b(100)(90))



# 1~100 사이의 숫자 중 5의배수를 출력하자.

# 3. e(i)애들을 받아올거야. 1부터 100까지 받아오겠지?
# 4. 1 % 5 = 4(true) / 2 % 5 = 3(true) / .... 5 % 5 = 0(false) 이런식으로 5의배수애들은 0이 될거야.
e = lambda x: bool(x % 5)
# 1. five라는 배열 안에서 1부터 100까지 for문을 돌려주겠어.
# 2. e(i)인 애들만. / 이 애들이 누군지 위에서 알 수 있어.
# 5. [ if e(i)인 경우 ] 여기서는 true인 애들만 담기겠지? || [ if not e(i)의 경우] 는 false인 애들만 담겨
five = [i for i in range(1, 101) if not e(i)]
print(five)

# 2. f는 파라미터 하나를 받아올건데 만일 내가 받아온 파라미터(x) % 5 가 0이 아닐 때 그 수를 return할거야.
#    그럼 5의배수가 아닌애들이 f로 들어가.
f = lambda x : x if (x % 5 != 0) else None # None라는애는 Null과 같아.
# 1. result라는 배열에 1부터 100까지의 수를 담을건데 만일 f(i)가 아닌애들만 담을거야..
# 3. 위에서 f는 5의 배수가 아닌애들을 담아왔어. 근데 현재 result의 if문에서 아닌애들으르 골랐으니까 5의배수인 애들을 담아준다는 뜻이지. 편하게 생각해서 not은 내가 구해온 결과값의 반대값이라고 생각해도 돼.
result = [i for i in range(1, 101) if not f(i)]
print(result)


# 위에 문장 하나로 합치기.
result_five = [i for i in range(1, 101) if not (lambda x: x if(x%5 != 0) else None)(i)]
print(result_five)











