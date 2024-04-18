import requests
from bs4 import BeautifulSoup as BS


class get_data_class:
    def __init__(self, attribute_value):
        self.attribute_value = attribute_value

    def connect_method(self):
        self.r = requests.get(self.attribute_value)

        r2 = str(self.r)

        if r2 == '<Response [200]>':
            atr_conection = 'connect OK!!!!!'

        return atr_conection

    def get_dir(self):
        html = BS(self.r.content, 'html.parser')
        self.listDir = []

        allDir = html.findAll('a')  # soup.findAll('a', class_='lenta')

        for data in allDir:
            self.listDir.append(data.text)

        return self.listDir

    def get_list_files(self,dir):
        self.listSec = []

        listDir = get_data_class.get_dir(self)

        # dir ='2024-04-15'
        # dir = listDir[len(listDir) - 1]

        r_dir = requests.get(f'http://erinrv.qscalp.ru/{dir}/')
        html = BS(r_dir.content, 'html.parser')
        allSec = html.findAll('a')

        for data in allSec:
            if data.get('href') != '/':
                self.listSec.append(data.text)

        # for link in html.find_all('a'):
        #     if link.get('href') != '/':
        #         print(link.get('href'))

        return self.listSec

    def download_file(self, r_dir):

        # Скачиваем файл
        # file1 = requests.get('http://erinrv.qscalp.ru/2024-04-16/VTBR.2024-04-16.Deals.qsh')
        file1 = requests.get(r_dir)

        # with open('Test_QSH/VTBR.2024-04-16.Deals.qsh', 'wb') as file:
        #     file.write(file1.content)
        return file1.content
