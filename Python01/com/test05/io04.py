# -*- coding:utf-8 -*-

file = open('test01.txt', 'a') # 이어쓰기
file.writelines('\nHello, Python!')
file.close()
