from data import get_data as gd

url = "http://erinrv.qscalp.ru/"
test = gd.get_data_class(url)
a = test.connect_method()
print(a)

