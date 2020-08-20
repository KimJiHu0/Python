# -*- coding:utf-8 -*-


def func01(x, y):
    sum = x + y
    return sum
    
    
def func02(x, y):
    return x+y,x-y
    
    
    
    
if __name__ == '__main__':
    a = func01(1,3)
    print(a)
    b= func02(4,7)
    print(b) # 얘는 Tuple
    c , d = func02(5, 3)
    print(c, d) # 얘는 Tuple에서 따로 빼준거야