# -*- coding:utf-8 -*-

# 개미수열 : 
'''
1
1 1
1 2
1 1 2 1
1 2 2 1 1 1
1 1 2 2 1 3
1 2 2 2 1 1 3 1
1 1 2 3 1 2 3 1 1 1
.......
'''

# 122111이 들어왔따 치자
def ant(i):
    # 1 기준 -> 몇개?
    # 2가 나오면 1기준으로 몇개가 있었는지를 결과에 추가
    # 2 기준 -> 몇개?
    # 1이 나오면 2 기준으로 몇개가 있었는지 결과에 추가
    # 1 기준 -> 몇개?
    # 결과에 추가
    # 리턴
    
    # 그럼 얘는 inp = 122111.
    inp = str(i) # 그냥 숫자로하면 11, 12,1121인데 list로해서 index로 찾아서 해보자 / 넘어온 값.
    # 얘는 그럼 1이야
    target = inp[0] # 가장 첫번째에 들어오는애. 
    cnt = 0
    res = ''
    for a in inp: # inp이라는애는 문자야. 안에있는 0번지 1번지 ... 까지 a로 들어가서 밑에 if문 실행.
        # 1 == 1 결과 후에 inp의 다음 index를 비교.
        if a == target:
            cnt += 1 # target과 같으면 cnt ++
        else : # 새로운 숫자가 나왔다면
            # '' += 1 + 1 (cnt는 str이니까)
            res += target + str(cnt) # cnt는 숫자니까 문자로 변환
            cnt = 1
            # target을 a로 바꿨으니까 2가 됐어.
            target = a
    res += target + str(cnt)
        
    return res
    

if __name__ == '__main__':
    n = int(input('ant stage : '))
    val = ant(1)
    
    print('1')
    print(val)
    for i in range(1, n):
        val = ant(val)
        print(val)
    