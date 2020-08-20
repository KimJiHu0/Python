# -*- coding:utf-8 -*-

#. for문을 사용해서 구구단을 전체 출력하는 함수 gugu()를 작성하고, main함수에서 호출
def gugu():
    for i in range(2,10): # 2부터 10-1 까지
        print('<<%d단>>' % i) # java에서 printf같은애야.
        for j in range(1,10):
            print('{} * {} = {}'.format(i, j, i*j))



#. while문을 사용하여 구구단 중 파라미터로 전달된 단만 출력하는 gugudan(x) 함수를 작성하고 main함수에서 호출
def gugudan(x): # 받아오는 타입은 int임
    i = 1
    print(x,'단')
    # 여기서 print해줄 때 [ x + 단 ]: int + string이기 때문에 안돼.
    # x를 형변환 해주던가, 아니면 x, '단' 으로 하던가
    while i < 10:
        print('{} * {} = {}'.format(x,i,int(x)*i))
        i+=1


#. 콘솔을 통해 n을 입력받아 호출하자
if __name__ == '__main__':
    n = input('구구단입력 : ')
    gugudan(n)
    gugu()
    gugudan(8)




