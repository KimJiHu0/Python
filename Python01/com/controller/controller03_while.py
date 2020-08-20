# -*- coding:utf-8 -*-

i = 1

while i < 10:
    print(i)
    i += 1
    # python에는 ++가 없어!


# while을 사용해서 1~10의 총 합계 출력

mysum = 0;
mycnt = 1
while mycnt <= 10:
    mysum += mycnt
    mycnt += 1
else:
    print('sum', mysum, sep='=')
    print('cnt', mycnt, sep='=')
