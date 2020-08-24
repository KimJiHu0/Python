# -*- coding:utf-8 -*-

import pickle

# 저장되어있는 딕셔너리 객체(바이너리로 바꿔서 저장한 test02.txt파일을 ) / r : 읽어올건데 / b : 바이너리인거를!
file =  open('test02.txt', 'rb')
# 그리고 score에 file을 담아조.
score = pickle.load(file)
# 그리고 닫아!
file.close()
# 그리고 출력해!
print(score)
