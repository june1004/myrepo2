#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:21:09 2020

@author: june
"""

## 01. URL 확보
## 02. URL에서 HTML 정보를 가져온다
## 03. 정보를 bs4를 이용하여 구조화
## 04. soup.find, soup.find_all 함수등을 이용해서 정보가져오기


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

page = urlopen(url)
#print(page)

soup =  BeautifulSoup(page, 'html.parser')

#%% 네이버 코스피, 코스닥, 코스피200 정보 가져오기
# ID는 유일한 값으로 일반적으로 class 의 id를 불러오는 형태로 작

kospi = soup.find("span", id="KOSPI_now").tex
print("현재 코스피지수는 {} 입니다." .format(kospi))

#%%
# 3-2 코스닥, 코스피200지수 가져오기

kosdaq = soup.find("span", id="KOSDAQ_now").text  
kpi200 = soup.find("span", id="KPI200_now").text

print("현재 코스닥지수는 {} 입니다." .format(kosdaq))
print("현재 코스닥지수는 {} 입니다." .format(kpi200))

#%%

#인기종목 10개
# tag = ul
# class : lst_pop

li_all = soup.find("ul", class_="lst_pop")
# print(li_all)

a_all = li_all.find_all("a")
li_span = li_all.find_all("span")


for i in a_all:
    print(i.text)

cnt = 0
for i in li_span:
    if cnt%2==0: 
        print(i.text)
        
    cnt = cnt + 1
#%%


