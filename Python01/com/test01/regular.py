# -*- coding:utf-8 -*-

# 정규식
import re # : re라는 애를 사용하겠다. re : 파이썬이 만든 모듈 (라이브러리)
'''
Regular Expression
. : 문자 1개를 의미
^ : 문자열의 시작을 의미
$ : 문자열의 마지막을 의미
[] : 문자 집합을 의미
| : or
() : 괄호 안 정규식 그룹
* : 0 또는 그 이상
+ : 1 또는 그 이상
? : 0 또는 1
{n} : n번 반복하라는 의미
{n,m} : n번부터 m번까지
{n, } : n번부터 무한대
'''

"""
r 문자열 표기법 (re모듈의 확장 문법)
\w : [a-zA-Z0-9_] : a~z, A~Z, 0~9, _를 포함하는 모든 문자
\W : [^a-zA-Z0-9_] : 위의 문자를 제외한 나머지 문자
\d : [0-9] : 0부터 9까지
\D : [^0-9] : 숫자를 제외한 나머지문자
\s : [\t\n\r\f\v] : 공백문자
\S : [^\t\n\r\f\v] : 위의 문자가 아니다.
\b : 단어의 시작과 끝의 빈 공백
\B : 단어의 시작과 끝이 아닌 빈 공백
\\ : \
\[n] : 지정된 n만큼 일치하는 문자열
\A : 문자열의 시작
\Z : 문자열의 끝

"""

str01 = '나의 이메일은 kh123@kh.com123 입니다.'
match = re.search(r'[\w]*@[a-zA-Z.]*', str01)
# [\w] : a-z, A-Z, 0-9까지를 구할건데
# * : 몇개든 상관이 없어.
# 그리고 그 뒤에 [a-zA-Z.] : a-z,A-Z, . 을 찾아 출력
print(match.group())
