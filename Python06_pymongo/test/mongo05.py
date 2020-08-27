# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

# 국어점수가 100점인애들 총점구하기
aggr = score.aggregate([
    {'$match':{'kor':{'$eq':100}}},
    {'$group':{'_id':'test', 'sum':{'$sum':'$kor'}}}
    ])

pprint.pprint(list(aggr))
