# -*- coding:utf-8 -*-

# Flask 모듈안에있는 Flask랑 request를 사용!
from flask import Flask, request

# 인스턴스 생성.
app = Flask(__name__)

# GET,POST 방식 전부 다 받을 수 있음
# a태그는 get방식이고 form태그는 post방식이다.
# return 값은 아래 지정한 변수 html이다.
@app.route('/', methods=['GET', 'POST']) 
def hello_root():
    html= '''
    <h1>Get or Post</h1>
    <a href="/test">get</a>
    <form action="/test" method="post">
        <input type="submit" value="post"/>
    </form>
    '''
    return html

# 이 route또한 GET방식과 POST방식을 전부 받을 수 있으며
# 위에서 get이라는 단어를 클릭해서 /test로 들어왔을 때 아래의 함수를 실행시켜준다.
@app.route('/test', methods=['GET', 'POST'])
def hello_test():
    # 만일 request의 method가 GET방식이라면 이 구문을 실행시켜주고, 
    if request.method=='GET':
        return '<h1 style="color:red;">Request Get</h1>'
    # 그게 아니라 request의 method가 POST라면 이 구문을 실행시켜준다.
    elif request.method=='POST':
        return '<h1 style="color:green;">Request Post</h1>'
    
    
if __name__ == '__main__':
    app.run()
