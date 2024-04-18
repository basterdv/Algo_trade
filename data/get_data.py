import requests
from bs4 import BeautifulSoup as BS


class get_data_class:
    def __init__(self, attribute_value):
        self.attribute_value = attribute_value

    def connect_method(self):
        r = requests.get(self.attribute_value)

        r2 = str(r)

        if r2 == '<Response [200]>':
            atr_conection = 'connect OK!!!!!'

        return atr_conection

# html = BS(r.content, 'html.parser')
# listDir = []
# listSec = []
#
# allDir = html.findAll('a')  # soup.findAll('a', class_='lenta')
#
# for data in allDir:
#     listDir.append(data.text)
#
# dir = listDir[len(listDir) - 1]
#
# r_dir = requests.get(f'http://erinrv.qscalp.ru/{dir}/')
# html = BS(r_dir.content, 'html.parser')
# allSec = html.findAll('a')
#
# for data in allSec:
#     listSec.append(data.text)
#
# for link in html.find_all('a'):
#     if link.get('href') != '/':
#         print(link.get('href'))

# Скачиваем файл
# file1 = requests.get('http://erinrv.qscalp.ru/2024-04-16/VTBR.2024-04-16.Deals.qsh')

# with open('Test_QSH/VTBR.2024-04-16.Deals.qsh', 'wb') as file:
#     file.write(file1.content)
