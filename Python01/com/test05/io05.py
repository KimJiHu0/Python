# -*- coding:utf-8 -*-

import pickle # 파이썬 객체 자체를 파일에 . unpickle = 반댄


# 딕셔너리 객체
score = {'name' : 'kh', 'kor' : 100, 'eng':99, 'math':56}

# 딕셔너리객체를 바이너리로 바꿔서 쓸꺼야!
with open('test02.txt', 'wb') as file: # 쓰긴할건데 바이너리형태로 쓸거임
    pickle.dump(score, file)