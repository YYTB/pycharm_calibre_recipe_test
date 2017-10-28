urlist = []
for nu in range(26,29):
    u = 'http://www.jxta.gov.cn/Column.shtml?p5='+str(nu)
    urlist.append(u)
    for n in range(2,3):
        urlist.append(u + '&p7=' + str(n))

print(urlist)