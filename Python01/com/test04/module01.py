# -*- coding:utf-8 -*-

# math라는 module를 import 가져온다.
# import math

# math에서 pi만 가져온다.
from math import pi

# 반지름을 넣으면 반지름을 구해주는 circle를 만들고싶어용ㅠㅠ
def circle(r):
    # pi * r * r = 반지름
    return pi * r * r


if __name__ == '__main__':
    r = int(input('원의 반지름 : '))
    print('반지름이 {}인 원의 넓이는 {}입니다.'.format(r, circle(r)))