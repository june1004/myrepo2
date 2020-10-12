# -*- coding: utf-8 -*-

#%%
from bs4 import BeautifulSoup

page = open("mypage.html", 'r', encoding="utf-8").read()     # 파일불러오기
print(page)

soup = BeautifulSoup(page, "html.parser")   # 데이터 구조화
print(soup)

#%%
# 헤드라인1을 가져오기


data = soup.find("h1")
print(data.text)

# 단락1 정보 가져오기
p1 = soup.find("p")
print(p1.text)

#%%

# 구글논문링크정보 가져오기

gg = soup.find("a")
print(gg.text)

#%%

# a 태그로 연결된 전체정보 가져오기

aa = soup.find_all("a")
print(aa)

#%%

# a 태그로 연결된 전체정보 가져오기

aa = soup.find_all("a")


for i in aa:
    print(i.text)
    
#%%

# p태그 전체정보 가져와서 text 출력

p_all = soup.find_all("p")

for i in p_all :
    print(i.text)
    
#%%
link_n = soup.find_all("a")

print(link_n[2].text)
