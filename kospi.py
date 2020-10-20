#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
# url 가져오기

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"

#%%

# BS를 통해 html 파싱하기
page = urlopen(url)
s = BeautifulSoup(page, "html.parser")
print(soup.title)
print(soup.title.text)

#%%
#거래량 및 거래대금 가져오기
# 태그/ID 찾기
# 거래량 : td, id : quant

deal = s.find("td", id = "quant")
print("오늘의 코스피 거래량 : ", deal.text)

deal_money = s.find("td", id = "amount")
print("오늘의 코스피 거래대금 : ", deal_money.text)



#%%
quant = s.find("td", id = "quant").text    #거래량(천주)
high_value = s.find("td", id = "high_value").text   #장중최고
low_value = s.find("td", id = "low_value").text   #장중최저
print(quant,\n high_value, low_value)

#%%


dat = s.find("div", class_="subtop_sise_detail")
high = dat.find_all("td", class_="td")[2].text
low = dat.find_all("td", class_="td2")[2].text


print("52주 최고", high)
print("52주 최저", low)
#%%

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000100"
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

print(soup.title)

#%%
# no_today 검색 - 한번에 검색

dat = soup.find('p', class_="no_today").find('span', class_='blind').text
print(dat)
#%%
# no_today 검색 동일(01)

dat = soup.find('p', class_='no_today')
dat01 = dat.find("span", class_="blind").text
print(dat01)