import linecache
import os.path
import os
ip_list = []
dict = {}
ipstr = linecache.getlines('cast.txt')
for ip in ipstr:
    ip_list.append(ip[0:-1])

for a in ip_list:
    name = a.split("\t")[0]
    t = a.split("\t")[1]
    if len(name) <6 and int(t) >3:
        dict[name] = t

sorted(dict)
for i in dict.keys():
    print(i + "\t" + dict.get(i))
    with open('tgtg.txt', 'a', encoding='utf-8') as file:
        file.write(i+ "\n")
