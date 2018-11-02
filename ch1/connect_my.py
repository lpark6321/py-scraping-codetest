import requests
from bs4 import BeautifulSoup
"""
resp = requests.get('https://jwlin.github.io/py-scraping-analysis-book/ch1/connect.html')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.find('h1').text)
"""
resp = requests.get('https://www.wenku8.net/modules/article/reader.php?aid=1787&cid=61148')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.text)
