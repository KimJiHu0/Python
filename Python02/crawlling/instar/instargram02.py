# -*- coding:utf-8 -*-

# selenium을 사용하는 이유 : 
# ajax뿐만 아니라 모든 랜더링이 실행 된 후에 크롤링을 하기 위해서 사용해준다.
# 내가 자동으로 걔를(브라우저를) 조작해주는 애?
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/explore/tags/' + input('search keyword : ')

# driver을 C:\test\에 있는 chromedriver.exe를 사용하겠다는 의미.
driver = webdriver.Chrome('C:/test/chromedriver.exe')
driver.implicitly_wait(3) # 3초 기다릴거야!
driver.get(url)

# soup변수에 driver.page_source를 html로 parser해준다.
soup = BeautifulSoup(driver.page_source, 'html.parser')
# img_List에는 크롤링해서 긁어온 html들 중(soup)에서 div태그  
img_List = soup.find_all('img')
# print(img_List)


# src경로만 뽑아오자.

# 위에서 찾은 img태그들을 전부 img_List에 담았는데
# m이라는 변수에 img_List를 하나하나 담아주고
# 그 m이라는 변수에 들어온 img태그의 src속성만 가져와서 출력해준다
for m in img_List:
    print(m.get('src'))



