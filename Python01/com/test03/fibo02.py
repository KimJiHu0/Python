# -*- coding:utf-8 -*-

# fibonacci 수열 출력하지
def fibo1(n):
    
    # 가장 처음 숫자.초기값
    a, b = 0, 1
    # 몇번 출력할건지 
    i = 0
    while i  < n:
        print(a, end=' ')
        a, b = b , a+b
        i += 1


# fibonacci 수열을 list에 담아서 return
def fibo2(n):
    a,b = 0, 1
    lst = list()
    i = 0
    while i < n:
        lst.append(a)
        a, b = b, a+b
        i += 1
    return lst
        


if __name__ == '__main__':
    n = int(input('n : '))
    fibo1(n)
    fibo = fibo2(n)
    print()
    print(fibo)
