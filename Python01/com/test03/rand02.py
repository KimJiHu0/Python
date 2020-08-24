# -*- coding:utf-8 -*-

import random

# 1부터 45 사이의 숫자 6개를 중복없이 만들어서 리스트로 리턴하는 lotto()함수 만들자
# main함수에서 호출하여 출력


# 로또라는 함수를 만들었다.
def lotto():
    # list 배열을 하나 선언해주었고
    list = []
    # for문을 6번 돌릴거야. (내가 6개 출력해줄거걸랑)
    for i in range(6):
        # 변수 a에 난수 1~45까지의 수를 만들어서 넣었는데 for문 밖에 쓰면 하나의 수가 똑같이 6번 반복되서
        # 새로운 난수를 넣어줄때마다 생성하게끔 for문 안에 넣어줬어 
        a = random.randint(1,45)
        # 만약에 list안에 a라는 1~45사이의 난수가 없다면
        if a not in list:
            # list에 a라는 변수를 append해줄거야!
            list.append(a)
        # 만일 list에 수가 겹친다면
        else :
            # 새로운 난수를 하나 만들어줄거야
            b = random.randint(1, 45)
            # 그리고 list에 b가 있는지 없는지 찾아줄거야. 그리고 새로운 난수 b가 list에 없다면
            while b not in list:
                # list에 b를 append해줄게
                list.append(b)

    # 그 다음에 list를 정렬한 후에
    list.sort()
    # return할거야
    return list

def lotto1():
    lotto = set()
    
    while len(lotto1) <= 6:
        ran = random.randint(1, 45)
        lotto1.add(ran)
        
    result = sorted(lotto1)
    print(result)


# 아래의 뜻은 main함수라는 뜻이야.
if __name__ == '__main__':
    #return했으니까 pinrt()로 lotto함수를 불러와
    print(lotto())
    
    print(lotto1())