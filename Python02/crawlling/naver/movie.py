# -*- coding:utf-8 -*-

# 파싱해주는애.
# html.parser를 사용할 수 있게 해주는거
# request했더니 response된 문서 data를 html.parser를 가지고 파싱해준거야.태그로 바꿔준거야
from bs4 import BeautifulSoup
import urllib.request # 파이썬 내부적으로 기본적으로 가지고있는 패키지. 내가 원하는 패키지랑 연결할 수 있어

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
# print(resp)
soup = BeautifulSoup(resp, 'html.parser')
# print(soup)

movies = soup.find_all('dl', class_='lst_dsc') # dl태그중에 class가 lst_dsc 가져옴
# print(movies)
# print(movies[0])



# 제목과 별점만 출력하자.
# dt태그 중 class이름이 tit인 애들 중에서 a태그인 애를 title에 담아서 출력
# title = soup.find('dt', class_='tit').find('a')
# print(title)

# div태그 중 class이름이 star_t1인 애 중에서 span태그이고 class이름이 num인 애를 star에 담고 출력
# star = soup.find('div', class_='star_t1').find('span', class_='num')
# print(star)

for movie in movies:
    title = movie.find('a').text # find 하나만쓰면 제일 위에있는 a태그만
    star = movie.find('span', class_='num').text
    print('{} [{}]'.format(title, star))