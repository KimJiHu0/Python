# -*- coding:utf-8 -*-

# 다운받은 flask import.
from flask import Flask

# flask를 사용하기 위해 인스턴스 생성하기
app = Flask(__name__)

# 가장 메인 화면인 곳의 route는 /이다.
# hello_root함수와 연동.
@app.route('/')
def hello_root():
    # return 구문에 href가 /test/admin 이다.
    # 이를 클릭하게 되면 url은 localhost:5000/test/admin 으로 이동할 것이다.
    return '<h1><a href="/test/admin">parameter test</a></h1>'

# 이곳에서는 /test/<id> 로 위에서 "parameter test"를 클릭했을 때 들어온 admin은 id로 (parameter)로 들어온다.
@app.route('/test/<id>')
# 함수에서도 id를 파라미터로 받아주었고, 
def hello_test(id):
    # return 값은 hello + id 이다. url을 확인해보면 localhost:5000/test/admin으로 되어있는데
    # admin부분을 바꿔서 입력하면 parameter값이 내가 입력한 값으로 나오는걸 볼 수 있다.
    return '<h1>hello, ' + id + '</h1> <a href="/">go root</a>'

if __name__ == '__main__':
    app.run()