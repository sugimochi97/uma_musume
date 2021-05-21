from bs4 import BeautifulSoup
import requests
import pandas as pd
from scraping import *

RACE_COLUMNS = ['年', '月', 'レース名', 'クラス', '場所', '距離', '回り']
OUTPUT_CSV = './race.csv'

load_url = URL
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

load_url = URL
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')
lis_td = []
lis_a = []
for element in soup.find_all(class_=RACE_CLASS):
    lis = [i.text for i in element.find_all('td')]
    lis_td.append(lis[0].split(' ') + lis[1].split(' / '))
    lis_a.append([i.text for i in element.find_all('a')])
while [] in lis_a:              # 空リストを削除する
    i = lis_a.index([])
    lis_a.pop(i)
    lis_td.pop(i)
lis_a = [i[1] for i in lis_a]
df = pd.DataFrame(lis_td, columns=RACE_COLUMNS)
se = pd.Series(lis_a)
df['レース名'] = se
df.to_csv(OUTPUT_CSV)