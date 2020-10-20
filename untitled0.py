#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:21:40 2020

@author: june
"""

#%%

from bs4 import BeautifulSoup

html = """
<html>
<head><title> test site </title></head>
<p class='class1' align="left">test3</p>
<p class='class1'>test2</p>
<p id='p1'>오늘의 주가지수 1500</p>
<span class='class3'>span tag text</span>
<p class='class4'>test3</p>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

print( list(soup.children)  )
print( list(soup.body.children)  )

#%%

from urllib.request import urlopen
from bs4 import BeautifulSoup

basic_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page=1"

url1 = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page=1"
page = urlopen(url1)
soup = BeautifulSoup(page, "html.parser")
comment_all = soup.find_all('td', class_='title')
print(comment_all)

#%%
print(len(comment_all))

#%%
print(comment_all[0])

#%%
ch_td = list(comment_all[0].children)
print(ch_td[6].strip())

#%%

cnt = 0
comments = []
for comment in comment_all:
    temp = list(comment.children)
    result = temp[6].strip()
    # print(result)
    comments.append(result)

print(comments)

#%% 여러개 댓글 가져오기
cnt = 0
comments = []
for comment in comment_all:
    temp = list(comment.children)
    result = temp[6].strip()
    # print(result)
    comments.append(result)

print(comments)