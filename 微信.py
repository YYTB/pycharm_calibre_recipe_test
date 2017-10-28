#coding=utf-8
import urllib,urllib2
import wechatsogou
import os


ws_api =wechatsogou.WechatSogouAPI(captcha_break_time=3)
url1=[]
gongzhonghao = ['南航青年志愿者','中国旅游报','宜春多胜游']
path = os.getcwd()
file_name=[]

#def downLoad(dest_dir, URL):
#    try:
#        urllib.urlretrieve(url, dest_dir)
#    except:
#        print '\tError retrieving the URL:', dest_dir






for hao in gongzhonghao:
    url1.append(ws_api.get_gzh_info(hao)['profile_url'])


for i in range(len(gongzhonghao)):
    dest_dir=os.path.join(path,str(i)+'.html')
for url in url1:
    urllib.urlretrieve(url, dest_dir)
        #continue
print(url1)

#downLoad('./wo.html','https://mp.weixin.qq.com/profile?src=3&timestamp=1507460232&ver=1&signature=OpcTZp20TUdKHjSqWh7m73RWBIzwYwINpib2ZktBkLG8NyHamTvK2jtzl7mf-Vdph2ADU9EfDRBvqhF4VwRLzQ==')









#print(path)

#path2 = 'hello'
#print(path2)
