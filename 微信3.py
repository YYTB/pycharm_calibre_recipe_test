#coding=utf-8
import urllib,urllib2
import wechatsogou
import os


ws_api =wechatsogou.WechatSogouAPI(captcha_break_time=3)
path = os.getcwd()

#一楼
gongzhonghao = '中国旅游报'

dest_dir=os.path.join(path,gongzhonghao+'.html')

ws_api.get_gzh_artilce_by_history(gongzhonghao)
#url = ws_api.get_gzh_info(gongzhonghao)['profile_url']

#urllib.urlretrieve(url, dest_dir)

