#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%%

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"

page = urlopen(url)
soup = BeautifulSoup(page, "lxml")

print( soup.title )

#%%

ul_one = soup.find("ul", class_="lst_detail_t1")
print( ul_one)

#%%
a_all = soup.find_all("a")
print(a_all)

#%%
# dt, class:tit
# a → text

li_all = ul_one.find_all("dt", class_="tit")
#print(li_all[1])

one_title = li_all[0].find("a")
print(one_title.text)

#%%

li_all = ul_one.find_all("dt", class_="tit")

for one in li_all:
    one_title = one.find("a").text
    print(one_title)


#%%
##  평정정보 가져오기

ul_one = soup.find("ul", class_="lst_detail_t1")

score_all = ul_one.find_all("span", class_="num")
print(score_all)

cnt = 1
for one in score_all:
    if cnt%2==0:
        print(one.text)
    cnt = cnt + 1
    
   #%%
   ## 예매율 가져오기

ul_one = soup.find("ul", class_="lst_detail_t1")

reserve_all = ul_one.find_all("span", class_="num")
print(reserve_all)

cnt = 0
for one in reserve_all:
    if cnt%3==1:
        print(one.text)
    cnt = cnt + 1


#%%

#01. 전체정보 가져오기
ul_one = soup.find("ul", class_="lst_detail_t1")

#02. div, class : star_t1
ul_02 = soup.find_all("div", class_="star_t1")
#print(ul_02[0])

#03. span, class : num
ul_03 = ul_02[2].find("span", class_="num")
print(ul_03.text)

#%%

cnt = 1
for one in ul_02:
    if cnt%2==0:
        print(one.find("spa", class_="num"))
    cnt = cnt + 1