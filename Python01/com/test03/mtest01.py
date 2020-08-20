# -*- coding:utf-8 -*-


# 함수 만들기

def fun01():
    print('fun01 입니다.')
    
def fun02():
    return 'fun02 입니다.'

def fun03():
    return {1:'a', 2:'b'}

if __name__ == '__main__':
    # 프로그램의 주 진입점 : main function
    print('프로그램 시작 시 가장 먼저 호출돼!')
    fun01()
    print(fun02())
    print(fun03()[1])