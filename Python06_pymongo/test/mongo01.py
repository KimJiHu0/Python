# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

# 클라이언트(mongoDB)와 파이썬을 연결
client = MongoClient('localhost', 27017)
# db는 연결된 몽고디비에 test를 의미
db = client.test
# score는 연결된 test에서 score를 사용하겠다는 의미
score = db.score


# cursor은 java에서 hasnext와 같은 의미를 지녀
# 가리키는 다음 위치를 말해
cursor = score.find()
print(cursor)

for doc in cursor:
    pprint.pprint(doc)
    
print('-----------')
    
# 하나만 가지고와도 cursor객체. 커서값이 출력돼
park = score.find({'name':'박진우'})    
print(park)

for doc in park:
    print(doc)
    
print('-----------')

# find_one은 해당 document를 가져와서 cursor에 안담겨
kang = score.find_one({'name':'강여림'})
print(kang)
pprint.pprint(kang)

print('-----------')
# 국어점수가 60보다 큰$gt를 이용해서 document 출력
# find는 cursor객체에 담겨. 그러니까 for문 돌려서 빼줘
people = score.find({'kor':{'$gt':60}})
for doc in people:
    pprint.pprint(doc)


print('총 갯수 : ', score.count_documents({}))

