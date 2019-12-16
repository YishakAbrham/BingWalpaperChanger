from bs4 import BeautifulSoup 
from datetime import datetime as dt
import requests
import urllib.request
import ctypes
import os
import random


res = requests.get('https://bing.wallpaper.pics/')
soup = BeautifulSoup(res.text,'lxml')
imageBox = soup.find('a',{'class':'cursor_zoom'})
image = imageBox.find('img')

link = image['src']

filename = 'desktop.jpg'
filename2 = 'desktop'+ str(random.randint(1,10000000000000))+'.jpg'

urllib.request.urlretrieve(link,filename)

urllib.request.urlretrieve(link,'E:\\Pictures\\Bing wallpapers\\'+filename2)

absolute_path=os.path.abspath("desktop.jpg")

ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path , 0)
