# -*- coding:utf-8 -*-

def mysum(x, y):
    return 2 * x + y


if __name__ == '__main__':
    print(mysum(2, 3))
    
    mysum01 = lambda x, y : 2 * x + y
    print(mysum01(2,3))
    # print((lambda x, y : 2 * x + y)(2, 3))