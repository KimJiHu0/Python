# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
import requests
import json # 크롤링 한 데이터를 json으로 바꿀게!

# resp라는 변수에 아래 url을 쓴다?는 의미로 봐도 될 듯
resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=mon')
# 그리고 soup에는 위에서 담은 resp.text를 html로 parser해줘
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)


# 크게 잡아서 ul태그 중 class속성이 lmg_list인 애들 webtoons에 담기
webtoons = soup.find('ul', {'class': 'img_list'})
# print(webtoons)

# webtoons안에서 dl이라는 변수에 dl태그들을 전부 담기
dl = webtoons.select('dl') # select : 태그명, id명, class명, 속성값, 구조적위치를 입력

lst = list()
# dl태그를 다 chd에 담고 for문을 돌릴건데
for chd in dl:
    # title이라는 변수에는 dl태그 안에 a태그의 text를 담을거고
    title = chd.find('a').text # 제목 담아줘
    # star이라는 변수에는 dl태그의 strong태그의 text를 담았다.
    star = chd.find('strong').text # 별점 담아줘
    # 그리고 {} [{}].format을 이용해 title, star을 담아주면 이쁘게 출력이 된다.
    print('{} [{}]'.format(title, star))
    tmp = {} # 딕셔너리
    tmp['title'] = title # title라는 key에 title 값 넣어주기
    tmp['star'] = star # star이라는 key에 star 값 넣어주기
    # {'title' : '제목', 'star' : '별점'...} 으로 담길거야
    lst.append(tmp)
# print(lst) 여기까진 json형태가 아님.
# [{'title' : '제목', 'star' : '별점'...},{'title' : '제목', 'star' : '별점'...}...]되어있는교
# 얘는 json이 아닌걸?

res = {}
res['webtoons'] = lst
# print(res) # 진짜 json 형태의 문자열 = 싱글 쿼테이션의 딕셔너리였음
 
# dumps : 바꾸는거
# ensure_adcii : 아스키코드로 바꾸는거
res_json = json.dumps(res, ensure_ascii=False)
# print(res_json) # json형태임 = 더블쿼테이션으로 바꿈


# json 파일 저장하기!
with open('webtoons.json', 'w', encoding='utf-8') as f:
    f.write(res_json)