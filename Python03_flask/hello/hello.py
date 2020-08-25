# -*- coding:utf-8 -*-

# Flask란 Micro Web Framework라고도 한다.
# 간단한 웹사이트, API를 만드는데 특화되어있는 Python Web Framework이다.
# 가벼운 기능을 제공하고, 확장성이 넓다.

# CMD에 pip install flask 를 치면 flask에 대한 것들을 다운로드 받을 수 있다.
from flask import Flask

# Flask의 인스턴스 생성
app = Flask(__name__)

# url이 / 인 것과 hello라는 함수랑 연동해주겠다는 의미이다.
# 우선적으로 route('/')가 의미하는 것은 가장 기본적인 화면을 의미한다.
@app.route('/hello')
def hello():
    # 아래의 함수가 실행되었을 때 Hello,World! 라는 문구가 return되어 화면에 나올 것이다.
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
