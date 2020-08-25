# -*- coding:utf-8 -*-

# flask 모듈 안에있는 render_template, request, flask를 사용하기 위해 import
from flask import Flask, render_template, request

# 인스턴스 생성
app = Flask(__name__)


@app.route('/')
def root():
    return '''
    <a href="/hello">hello</a><br/>
    <input type="button" value="hello" onclick='location.href="/hello/name"'/>
    '''

# 그냥 hello로 넘어오든 (값이 안넘어와서 name 은 None)
# <name>이 같이 넘어와도 받아준다. (해당 값으로 치환)
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    # hello.html을 render_template를 통해서 화면에 그려줄건데 name=name / name이라는 이름으로 name을 전달
    # request.setAttribute("name", name)이랑 비슷한 느낌이야.
    # template으로 만들어놓은 html을 구현시켜준거야
    return render_template("hello.html", name=name)


# post방식으로 test라는 이름으로 넘어왔을 때 이 함수 실행
@app.route('/test', methods=['POST'])
def test():
    # 받은 command 그대로 test에 담아서 test.html에 request해준다(보내준다)
    return render_template("test.html", test=request.form['command'])


if __name__ == '__main__':
    # host와 port 지정해주기
    app.run(host='localhost', port='8585')