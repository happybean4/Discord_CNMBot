from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib import request
from urllib.request import Request, urlopen


def schedule():
    url = "https://chungnamms.djsch.kr/scheduleH/list.do?section=1&schdYear=2021"
    url2 = "https://chungnamms.djsch.kr/scheduleH/list.do?section=2&schdYear=2021"
    hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')} 
    req = requests.get(url , headers=hdr) 
    html = req.text 
    soup = BeautifulSoup(html, 'html.parser')



    temp = 0
    ls = [[] for _ in range(12)]
    n =3
    x = 0


    for i in soup.select('dl[class=event]'):   # 3월 ~8월
        x = i.text.replace(' 행사내용   ','').replace('\xa0',' ').replace('   ','')
        cnt = x.count(':')
        for j in range(cnt-1):
            end = x.find(':',x.find(':')+1)-4
            end = end if x[end] != '~' else end-3
            ls[temp].append(str(n)+'월'+x[:end])
            x = x[end:]
        ls[temp].append(str(n)+'월'+x)
        temp+=1
        n = (n+1 if n != 12 else 1)



    for i in soup.select('dl[class=event]'):   # 
        x = i.text.replace(' 행사내용   ','').replace('\xa0',' ').replace('   ','')
        cnt = x.count(':')
        for j in range(cnt-1):
            end = x.find(':',x.find(':')+1)-4
            end = end if x[end] != '~' else end-3
            ls[temp].append(str(n)+'월'+x[:end])
            x = x[end:]
        ls[temp].append(str(n)+'월'+x)
        temp+=1
        n = (n+1 if n != 12 else 1)
    return ls