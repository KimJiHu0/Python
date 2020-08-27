# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

# name이 자기이름인 애 삭제 
deleteone = score.delete_one({'name':'김지후'})
print('삭제갯수', deleteone.deleted_count)

# name이 존재하는애들 다 삭제
deletemany = score.delete_many({'name':{'$exists':'true'}})
print('삭제갯수', deletemany.deleted_count)
