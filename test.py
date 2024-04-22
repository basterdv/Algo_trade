from data import get_data as gd

url = "http://erinrv.qscalp.ru/"
test = gd.get_data_class(url)
a = test.connect_method()
print(a)

dirs = test.get_dir()

# for dir in dirs:
#     print(dir)

dir = '2024-04-16'
files = test.get_list_files(dir)

# for file in files:
#     print(file)

r_dir = 'http://erinrv.qscalp.ru/2024-04-16/VTBR.2024-04-16.Deals.qsh'
download_file = test.download_file(r_dir)
with open('C:/Users/Home/Downloads/VTBR.2024-04-16.Deals.qsh', 'wb') as file:
    file.write(download_file)
