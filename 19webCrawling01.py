import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
response = requests.get(url)

if response.status_code==200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    #셀렉터로 추출(크롬)
    title1_1 = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt')
    print("추출1:", title1_1)
    
    text = title1_1.get_text()
    print("추출2:", text)
    
    ul = soup.select_one('ul.basic1')
    print("추출3:", ul)

    #print("추출4")
    titles2 = ul.select('li > dl > dt > a')
    for tit in titles2:
        print(tit.get_text())
else:
    print(response.status_code)


