# 문자 (single quotation / double quotation의 차이 없음)

#single * 1
a = 'Hello, Python!'
print(a)

#TEST : ''안에 ''쓰기 / 역슬레쉬를 붙여주면 돼.
test = 'python\'s \n Hello,World!'
print(test)


#single * 3 : 작성한 그대로 전부 출력. HTML에서 pre태그와 비슷하다고 봐.
b='''python's
Hello,World!       !!!!
    Hello,Python'''
print(b)

# double * 1 : 더블쿼테이션에서는 싱글퀘테이션에 역슬레쉬 안붙여도 돼!
c = "python's\nHello,World!"
print(c)

#Test : "" 안에 ""넣기. 이 경우에는 역슬레쉬를 붙여주면돼.
test1 = "python's \n \"Hello,World!\""
print(test1)

# double * 3 : 쓰는대로 출력이 돼. 역슬레쉬같은거 필요없어.
d = """python's "Hello, World!" """
print(d)
