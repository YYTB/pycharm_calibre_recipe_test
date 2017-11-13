#coding=utf-8
import datetime


today = datetime.date.today()-datetime.timedelta(days= 5*7)#datetime.date.today()  # 获取当前日期, 因为要求时分秒为0, 所以不要求时间
weekday = today.weekday()  # 获取当前周的排序, 周一为0, 周日为6
# 旅游报周一到周五发行，以下算出日期区间
last_monday_delta = weekday + 7  # 当前日期距离上周一的天数差
last_friday_delta = weekday + 3  # 当前日期距离上周五的时间差

print(datetime.date.today() - datetime.timedelta(days = last_friday_delta))

riqilist = []
for nu in range(last_friday_delta,last_monday_delta + 1):
    riqi = today- datetime.timedelta(days = nu)
    riqilist.append(str(riqi))
print(riqilist)

print(datetime.date.today()-datetime.timedelta(days= 5*7))