# -*- coding:utf-8 -*-
from com.test05.io01 import file

# close안하고 with해주면 close를 안해줘도 자동으로 close를 해줘! java에서 try(){}catch{}랑 같아
with open('test01.txt', 'r') as file:
    a = file.read()
    print(a)
