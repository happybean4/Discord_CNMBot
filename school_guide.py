import requests
from bs4 import BeautifulSoup

def title(list, int_v):
    int_a = int_v-1
    td_list = list[int_a:int_v]
    
    for td in td_list:
        a = td.find('a')
        title = a.attrs['title']
        return title

def js(list, int_v):
    int_a = int_v-1
    td_list = list[int_a:int_v]
   
    for td in td_list:
        a = td.find('a')
        js = a.attrs['onclick']
        js = js.split("'")
        return js

def url(js):
    a = js[1]
    b = js[3]
    c = js[5]
    d = js[7]
    e = js[9]
    f = js[11]
    g = js[13]
    h = js[15]
    url = """https://chungnamms.djsch.kr/boardCnts/view.do?boardID={}&boardSeq={}&lev={}&searchType={}&statusYN={}&page={}&pSize={}&s=chungnamms&m=0203&opType={}""".format(a, b, c, d, e, f, g, h)
    return url

def school_gt(int_number):   #notification title
    html = requests.get("https://chungnamms.djsch.kr/boardCnts/list.do?type=default&page=1&m=0203&lev=0&s=chungnamms&boardID=51642")
    soup = BeautifulSoup(html.text, "html.parser")
    html.close()
    datal_list = soup.findAll('div', {'class': 'board-text'})
    td_list = []
    for datal in datal_list:
        td_list.extend(datal.findAll('td', {'class': "link"})) # 공지 리스트 출력


    title_g = title(td_list, int_number)
    return title_g


def school_gu(int_number):  #notification URL
    html = requests.get("https://chungnamms.djsch.kr/boardCnts/list.do?boardID=51642&m=0203&lev=0&s=chungnamms#contents")
    soup = BeautifulSoup(html.text, "html.parser")
    html.close()
    datal_list = soup.findAll('div', {'class': 'board-text'})
    td_list = []
    for datal in datal_list:
        td_list.extend(datal.findAll('td', {'class': "link"})) # 공지 리스트 출력

    url_g = url(js(td_list, int_number))
    return url_g


def notify(num):  #school_gu, school_gt 통합
    html = requests.get("https://chungnamms.djsch.kr/boardCnts/list.do?boardID=51642&m=0203&lev=0&s=chungnamms#contents")
    soup = BeautifulSoup(html.text, "html.parser")
    html.close()
    datal_list = soup.findAll('div', {'class': 'board-text'})
    td_list = []
    for datal in datal_list:
        td_list.extend(datal.findAll('td', {'class': "link"})) # 공지 리스트 출력
    return [title(td_list, num),url(js(td_list, num))]

def notifyAll(page):
    html = requests.get("https://chungnamms.djsch.kr/boardCnts/list.do?type=default&page="+str(page)+"&m=0203&lev=0&s=chungnamms&boardID=51642")
    soup = BeautifulSoup(html.text, "html.parser")
    html.close()
    datal_list = soup.findAll('div', {'class': 'board-text'})
    td_list1 = []
    for datal in datal_list:
        td_list1.extend(datal.findAll('tbody'))
    ls = td_list1[1].findAll('td',{'class':"link"})
    notiList = []
    
    for i in range(len(ls)):
        x = []
        try:
            for td in [ls[i]]:
                a = td.find('a')
                title = a.attrs['title']
                x.append(title)
            for td in ls[i]:
                js = a.attrs['onclick']
                js = js.split("'")
                x.append(url(js))
        except:
            print(i)
            break
        notiList.append(x)
    return notiList

def school_gtcon():
    html = requests.get("https://chungnamms.djsch.kr/boardCnts/list.do?boardID=51642&m=0203&lev=0&s=chungnamms#contents")
    soup = BeautifulSoup(html.text, "html.parser")
    html.close()
    datal_list = soup.findAll('div', {'class': 'board-text'})
    td_list = []
    for datal in datal_list:
        td_list.extend(datal.findAll('tr', {'bgcolor': "#EFF8FF"})) # 공지 리스트 출력
    gcon = len(td_list) # 공지 수
    return int(gcon)


def school_gtall():
    html = requests.get("https://chungnamms.djsch.kr/boardCnts/list.do?boardID=51642&m=0203&lev=0&s=chungnamms#contents")
    soup = BeautifulSoup(html.text, "html.parser")
    html.close()
    datal_list = soup.findAll('div', {'class': 'board-text'})
    td_list = []
    for datal in datal_list:
        td_list.extend(datal.findAll('tr')) # 공지 리스트 출력
    gcon = len(td_list) # 전체 공지 수
    return int(gcon)


def school_gtnormal():
    html = requests.get("https://chungnamms.djsch.kr/boardCnts/list.do?type=default&page=1&m=0203&lev=0&s=chungnamms&boardID=51642")
    soup = BeautifulSoup(html.text, "html.parser")
    html.close()
    datal_list = soup.findAll('div', {'class': 'board-text'})
    td_list = []
    td_list1 = []
    for datal in datal_list:
        td_list.extend(datal.findAll('tr', {'bgcolor': "#EFF8FF"})) # 공지 리스트 출력

    for datal in datal_list:
        td_list1.extend(datal.findAll('tbody')) # 일반 공지 리스트 출력

    gcon1 = len(td_list) # 공지 수
    gcon2 = len(td_list1) # 일반 공지 수

    
    return gcon2

