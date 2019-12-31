from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
def setting(name):
    
    url = "https://www.op.gg/champion/"+name+"/statistics/"
    hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36')} 
    response = requests.get(url,headers = hdr)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    returnValue={}

    
    table = soup.select('table.champion-overview__table.champion-overview__table--summonerspell > tbody:nth-child(5) > tr > td.champion-overview__data > ul > li > span')

    #스킬
    skill=""
    for x in table:
        skill+=x.text
        skill+=" "
    skill.rstrip()
    returnValue["skill"]=skill

    #소환사 주문
    spell=""
    table = soup.select('table.champion-overview__table.champion-overview__table--summonerspell > tbody:nth-child(3) > tr:nth-child(1) > td.champion-overview__data > ul > li > img')
    for x in table:
        x=str(x).split('&gt;')
        y=len(x[1])
        spell+=(x[1][0:y-6])
        spell+=", "
    spell.rstrip()
    returnValue["spell"]=spell

    #시작아이템
    startItem=""
    table = soup.select('table:nth-child(2) > tbody > tr:nth-child(1) > td.champion-overview__data.champion-overview__border.champion-overview__border--first > ul > li.champion-stats__list__item')
    for x in table:
        x=str(x).split('&gt;')
        y=len(x[1])
        startItem+=x[1][0:y-6]
        startItem+=", "
    startItem.rstrip()
    returnValue["startItem"]=startItem

    #추천빌드
    table = soup.select('tbody > tr:nth-child(3) > td.champion-overview__data.champion-overview__border.champion-overview__border--first > ul > li.champion-stats__list__item')
    recommendItem=""
    for x in table:
        x=str(x).split('&gt;')
        y=len(x[1])
        recommendItem+=x[1][0:y-6]
        recommendItem+=", "
    recommendItem.rstrip()
    returnValue["recommendItem"]=recommendItem

    #룬
    #메인룬
    mainfns=""
    subfns=""
    wkqfns=""
    table = soup.select('table > tbody.tabItem.ChampionKeystoneRune-1 > tr:nth-child(1) > td.champion-overview__data > div > div > div.perk-page__row > div > img')
    for x in table:
        x=str(x).split('&gt;')
        y=len(x[1])
        mainfns+=x[1][0:y-6]
        mainfns+="  "
    mainfns.rstrip()

    table = soup.select('div.perk-page__item--active > div > img')
    for x in table:
        x=str(x).split('&gt;')
        y=len(x[1])
        subfns+=x[1][0:y-6]
        subfns+="  "
    subfns.rstrip()
    
    mainRune=[mainfns.split("  ")[0],subfns.split("  ")[0],subfns.split("  ")[1],subfns.split("  ")[2],subfns.split("  ")[3]]
    returnValue["mainRune"]=mainRune
    
    subRune=[mainfns.split("  ")[1],subfns.split("  ")[4],subfns.split("  ")[5]]
    returnValue["subRune"]=subRune
    


    table = soup.select('div.perk-page__image > img.active')
    for x in table:
        x=str(x).split('&gt;')
        z=x[4].split('&')
        if z[0] == "+10% Attack Speed":
            wkqfns+="Attack Speed"
        elif z[0] == "+6 Armor":
            wkqfns+="Armor"
        elif z[0] == "Adaptive Force +9":
            wkqfns+="Adaptive Force"
        else:
            wkqfns+=z[0]

        wkqfns+="  "

    wkqfns.rstrip()
    extraRune=[wkqfns.split('  ')[0].split('+')[0],wkqfns.split('  ')[1].split('+')[0],wkqfns.split('  ')[2].split('+')[0]]
    returnValue["extraRune"]=extraRune
    return returnValue

