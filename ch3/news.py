import requests
import json
from bs4 import BeautifulSoup


def main():
    print('蘋果今日焦點')
    dom = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/headline').text
    soup = BeautifulSoup(dom, 'lxml')
    news=[]
    for ele in soup.find('ul', 'all').find_all('li'):
        new=dict()
        a=ele.find('div', 'aht_title_num').text,
        b=ele.find('div', 'aht_title').text,
        c=ele.find('div', 'aht_pv_num').text
        print(a,' ',b,' ',c)

        new['title_num'] = a
        new['title'] = b
        new['pv_num'] = c
        news.append(new)

    with open('new.json', 'w', encoding='utf-8') as f:
        json.dump(news, f, indent=2, sort_keys=True, ensure_ascii=False)
    print('-----------')
    print('自由今日焦點')
    dom = requests.get('http://news.ltn.com.tw/list/newspaper').text
    soup = BeautifulSoup(dom, 'html5lib')
    for ele in soup.find('ul', 'list').find_all('li'):
        print(ele.find('a', 'tit').text.strip())


if __name__ == '__main__':
    main()

