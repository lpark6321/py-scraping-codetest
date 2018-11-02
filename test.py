import time, requests, json, re, os, opencc, urllib.request
import multiprocessing as mp
from bs4 import BeautifulSoup
from collections import Counter
from urllib.request import urlopen, urljoin
def test1():
    scale = 50
    print("执行开始".center(scale // 2, "-"))  # .center() 控制输出的样式，宽度为 25//2，即 22，汉字居中，两侧填充 -
    start = time.perf_counter()  # 调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。两个函数取差，即实现从时间点B1到B2的计时功能。
    for i in range(scale + 1):
        a = '*' * i  # i 个长度的 * 符号
        b = '.' * (scale - i)  # scale-i） 个长度的 . 符号。符号 * 和 . 总长度为50
        c = (i / scale) * 100  # 显示当前进度，百分之多少
        dur = time.perf_counter() - start  # 计时，计算进度条走到某一百分比的用时
        print("\r{:^3.0f}% [{}->{}] {:.2f}s".format(c, a, b, dur),end='')# \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；{:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；{}，对应输出的数为a；{}，对应输出的数为b；{:.2f}，输出有两位小数的浮点数，对应输出的数为dur；end=''，用来保证不换行，不加这句默认换行。
        time.sleep(0.1)  # 在输出下一个百分之几的进度前，停止0.1秒
    print("\n" + "执行结果".center(scale // 2, '-'))
'''-----------------------------------------------------------------------------------------------------------------'''
base_url = 'https://morvanzhou.github.io/'
def crawl(url):
    response = urlopen(url)
    # time.sleep(0.1)             # slightly delay for downloading
    return response.read().decode()

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])   # 去重
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url

def multicore():
    pool = mp.Pool(processes=1) # 定义CPU核数量为3
    res = pool.map(job, range(10))
    print(res)
    multi_res = [pool.apply_async(job, (i,))for i in range(10)]
    # 用get获得结果
    print([res.get()for res in multi_res])
def job(x):
    return x*x

'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
if __name__ == '__main__':
    start = time.perf_counter()
    multicore()
    dur = time.perf_counter() - start  # 计时，计算进度条走到某一百分比的用时
    print("已花費{:.2f}s".format(dur))