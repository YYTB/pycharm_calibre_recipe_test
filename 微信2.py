#coding=utf-8
import urllib,urllib2,time
import wechatsogou
import os
import requests
from selenium import webdriver


ws_api =wechatsogou.WechatSogouAPI(captcha_break_time=3)
url1=[]
gongzhonghao = ['南航青年志愿者','中国旅游报','宜春多胜游']
hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
browser = webdriver.Chrome('/home/suchao/chromedriver')

for hao in gongzhonghao:
    url1.append(ws_api.get_gzh_info(hao)['profile_url'])

    for url in url1:
        #browser.get(url)
        print(url)

#    time.sleep(5)
#    for url in url1:
#        response = requests.get(url,headers = hea)
#    print response.text
