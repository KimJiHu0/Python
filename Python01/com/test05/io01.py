# -*- coding:utf-8 -*-


# io => 입출력

'''
io 모드

r : 읽기
w : 쓰기 (기존 내용 덮어쓰기)
a : 쓰기(기존 내용 이후에 이어서쓰기)
x : 새로운파일 만들어서 쓰기(이미 파일이 있으면 error)
t / b : text / binary (default : t) 
'''

file = open('test01.txt', 'w') # 파일이름 , 모드
file.write('Hello, World!')
file.close()

