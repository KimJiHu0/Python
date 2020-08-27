# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

# name이 김지후인 애 하나 국어점수 0점으로 바꾸기
# 찾은 갯수, 바꾼 갯수 출력
updateone = score.update_one({'name':'김지후'}, {'$set':{'kor':0}})
print('찾은갯수',updateone.matched_count)
print('바꾼갯수',updateone.modified_count)

# 수학점수가 100점인 애들 0점으로  바꾸기
updatemany = score.update_many({'math':{'$eq':100}}, {'$set':{'math':0}})
print('찾은갯수', updatemany.matched_count)
print('바꾼갯수', updatemany.modified_count)
# 찾은 갯수, 바꾼 갯수 출력