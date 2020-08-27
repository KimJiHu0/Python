# -*- coding:utf-8 -*-

# cmd에 pip install pymonggo를 치면 pymongo에 대한 모든 것을 다운받을 수 있음
from pymongo import MongoClient

# 클라이언트 mongoclient를 연결하는데 / mongoDB랑 Python이랑 연결
client = MongoClient('localhost', 27017)

# db는 연결된 db이름을 작성
# 우리는 mongoDB에서 test라는 이름으로 작성을 해왔으니까 test라고 적는다.
# 연결된 client에서 db랑 연결
# db = client['test'] 도 가능
# db는 연결된 mongoDB에서 test를 쓰겠다는 의미.
db = client.test
# collection은 연결된 db에서 score이라는 collection을 사용하겠다.
collection = db.score

# collection에서 find명령어를 쓴다.
for doc in collection.find():
    print(doc)