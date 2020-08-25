# -*- coding:utf-8 -*-

# flask모듈에 있는 flask, render_template 사용
from flask import Flask, render_template
# BeautifulSoup 사용 : 크롤링을 하기 위해서 사용한다고 봐도 무방. 어떠한 것을 html로 parser해주기 위해.
from bs4 import BeautifulSoup
import requests
import json
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)

# 처음 화면을 키고 브라우저를 접속했을 때 나오는 화면.
# render_template로 index.html 띄어줌.
@app.route('/')
def root():
    return render_template("index.html")
    

# template안에있는 index.html에서 crawling을 클릭하게 되면 "/crawling"경로를 타고 이곳으로 와서 함수를 실행.
@app.route('/crawling')
# http://127.0.0.1:8585/crawling링크로 요청을 하면 return이 json이라서 json을 응답해줄거야.
def crawling(): 
    # resp에 영화의 제목과 별점을 가져오기 위한 url을 입력해준다.
    resp = requests.get('https://movie.naver.com/movie/running/current.nhn#')
    # 그 url이 담긴 resp의 text를 html로 parser해준다.
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    # naver 영화에서, 제목과 별점을 크롤링하여 json으로 리턴하자.
    # { movies : [{"title" : '다만 악에서 구하소서', "star" : '7.79'}, {...}, {...}, ...]}
    
    # dl태그 중에서 class이름이 lst_dsc인 애들을 movies에 담았다.
    movieall = soup.find_all('dl', class_='lst_dsc')
    
    # 얘는 배열이라 [] 로 나와
    movies = list()

    # 위에서 찾은 movieall이라는 애들을 하나씩 movie에 담을거다.
    for movie in movieall:
        # 그 중에서 title이라는 이름으로 하나 담은 movie에 a태그를 찾아서 담고,
        title = movie.find('a').text
        # star이라는 변수에 movie의 span태그이고 class이름이 num인애의 text를 담는다.
        star = movie.find('span', class_='num').text
    
        # 딕셔너리 {}로 나와
        tmp = {} # tmp = dict()와 같은 의미.
        # 딕셔너리의 이름은 title이라는 이름으로 위에서 담은 title값을 넣어준다.
        tmp['title'] = title
        # 딕셔너리의 이름은 star, 위에서 찾은 star를 넣어준다.
        tmp['star'] = star
        # 그 후에 movies라는 list에 딕셔너리 tmp를 append해준다.
        movies.append(tmp)
    
    # 위까지 했다고 아직 끝난게 아니다. [{"title" : '다만 악에서 구하소서', "star" : '7.72'}, ...]식으로 나올거다.
    # json 형태로 뽑기 위해서는 key 값이 하나 더 있어야한다.
    
    # 다시한번 res라는 딕셔너리를 만들어주고,
    res = {}
    # res 딕셔너리의 이름을 movies라는 이름으로 하고 movies를 넣어준다.
    res['movies'] = movies
    
    # res를 json으로 바꿔준다.
    res_json = json.dumps(res, ensure_ascii=False)
    print(res_json)
    
    # 그리고 return값을 res_json
    return res_json
    
    
    
    
if __name__ == '__main__':
    # app를 실행해줄건데 port는 8585이다.
    app.run(port='8585')