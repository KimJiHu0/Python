# -*- coding:utf-8 -*-

# pip install numpy => 수치해석에 중요한 lib
# pip install matplotlib => 그래프 그릴때 많이 써.

import numpy as np # => numpy를 쓸건데 np라는 이름으로 쓸거야 (뱔칭)
import matplotlib.pyplot as plt # => matplotlib안에 pyplot만 쓸거야 이름은 plt
import random
from unicodedata import category

# 선그래프
def plt01():
    x = np.arange(1, 11)
    y = x
    
    plt.plot(x, y) # => 선그래프
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend([ 'y=x' ])
    plt.show()
    
# 막대그래프
def plt02():
    y = [random.randint(0, 10) for i in range(10)]
    x = range(10)
    
    plt.bar(x,y) # => 막대그래프
    plt.xticks(range(11))
    plt.yticks(range(11))
    plt.show()
    
    
# 원그래프
def plt03():
    data = [random.randint(100,1000) for i in range(4)]
    
    plt.pie(data)
    category = ['frist', 'second', 'third', 'fourth']
    plt.legend(category)
    plt.show()

if __name__ == '__main__':
    # plt01()
    # plt02()
    plt03()