# -*- coding:utf-8 -*-


# CMD에서 pip install flask해서 다운 받은 것은 import해준다.
from flask import Flask

# 인스턴스 생성을 해준 후에
app = Flask(__name__)

# 가장 메인 화면이라고 볼 수 있는 route('/')와 hello_root라는 함수를 연동시켜준다.
# 가장 메인 화면에 들어가면 hello_root함수를 실행시켜준다.
@app.route('/')
def hello_root():
    # return 구문을 보면 a태그로 href="/flask"라고 작성되어있는데
    # 이를 클릭하게 되면 /flask경로로 들어가서,  
    return '<h1><a href="/flask">hello, flask</a></h1>'

# 이곳에 있는 route('/flask')인 곳으로 이동이 된다.
# 그럼 이와 연동이 되어있는 hello_flask함수를 실행시키게 된다.
@app.route('/flask')
def hello_flask():
    # return에 href값이 /로 지정되어있기 때문에 다시 메인화면으로 돌아가는 것을 의미한다.
    return '<h1><a href="/">go root</a></h1>'


if __name__ == '__main__':
    app.run()