# -*- coding:utf-8 -*-

from pymongo import MongoClient

# 파이썬과 몽고디빙(클라이언트) 연결
client = MongoClient('localhost', 27017)
# db는 몽고디비에 test 사용
db = client.test
# score는 test에 있는 score 사용
score = db.score

# {name : 자기이름, kor : ?, eng : ?, math : ?} 등록

# insert_one이라는 객체를 return해서
# <pymongo.results.InsertOneResult object at 0x000001C0D74AD140> 출력
insertone = score.insert_one({'name':'김지후', 'kor':100, 'eng':100, 'math':100})

# 아래의 경우 insert할 떄 자동으로 지정해준 _id의 값이 출력
# print(insertdoc.inserted_id)
print(insertone)



# 여러사람 등록
insertmany = score.insert_many([
    {'name':'강여림', 'kor':100, 'eng':100, 'math':100},
    {'name':'위영석', 'kor':100, 'eng':100, 'math':100},
    {'name':'박진우', 'kor':100, 'eng':100, 'math':100}
    ])
# insert_many라는 객체를 return
# insert된 애들의 임의로 지정해준 _id를 출력
print(insertmany.inserted_ids)