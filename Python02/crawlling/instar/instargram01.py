# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

# url 뒷부분을 보면 키워드가 javascript면 그에 대한 검색결과 나와서 이렇게 해줬음
tag = input('search keyword : ')
url = 'https://www.instagram.com/explore/tags/python/?hl=ko' + tag
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

res = soup.find('div', {'class' : 'KL4Bh'})
print(res) # 이렇게하면 None나와ㅜㅜ /
# ajax라서 그런가봐. ajax가 실행될떄까지 멈췄다가 실행시켜줘야해 : selenium
# 꼭 ajax뿐만아니라 브라우저에서 랜더링이 다 된 후에 크롤링 하기 위해서 selenium을 써야해
