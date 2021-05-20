from bs4 import BeautifulSoup
import requests
import csv
from scraping import *

load_url = URL
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

csv_file = open('./race.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)


for element in soup.find_all(class_=RACE_CLASS):
    lis = [i.text for i in element.find_all('td')]
    lis = lis[0].split(' ') + lis[1].split(' / ')
    csv_writer.writerow(lis)

csv_file.close()