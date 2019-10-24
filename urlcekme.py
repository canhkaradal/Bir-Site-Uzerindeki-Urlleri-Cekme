import requests
from bs4 import BeautifulSoup
dosya=open("urller.txt","w",encoding="utf-8")
isimler= list()
a=input("Urliniz:")
metin="https://"+a
r = requests.get(metin)
source = BeautifulSoup(r.content,"lxml")
melisa = source.find_all('a')
for link in melisa:
    isimler.append(link.get('href'))

for i in range(len(isimler)):
    if(a in str(isimler[i])):
        dosya.write(str(isimler[i]))
        dosya.write("\n")