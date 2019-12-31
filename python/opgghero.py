from urllib.request import urlopen
from bs4 import BeautifulSoup
from opgg import setting
import pymysql

import requests


db=pymysql.connect(host='localhost',user='root',password='Gkstm785gkstm@',db='my_db',charset='utf8',port=3306)


url = "https://www.op.gg/champion/statistics"
hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36')} 
response = requests.get(url,headers = hdr)
html = response.text
soup = BeautifulSoup(html, "html.parser")





champion=[]
datab={}
cursor = db.cursor()

for tag in soup.select('div[class=champion-index__champion-item__name]'):
   champion.append(tag.text)

for x in champion:
    print(x)
    if x=='트런들':
        print('sex')
    else :
        datab[x]=setting(x)
        sql = "INSERT INTO hero VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (str(x), str(datab[x]['skill']),str(datab[x]['startItem']),str(datab[x]['recommendItem']),str(datab[x]['mainRune']),str(datab[x]['subRune']),str(datab[x]['extraRune']),str(datab[x]['spell'])))
    #print(datab[x]['skill'])
    #print(datab[x])

db.commit()

# DB 연결 닫기
db.close()
