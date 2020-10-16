import linecache


def writetotxt(filename, str):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(str)
        file.write('\n')


lines = linecache.getlines('D:\data\AB\ehdata')
fu = ' '
for line in lines:
    sp = line.split(',')
    try:
        # if float(sp[15]) > 4.85 and int(sp[4])>500 and int(sp[4]) >500:
        if int(sp[3])>5000:
            print(sp[0] + fu + sp[15] + fu + sp[4] + fu + sp[3] + fu + sp[-1][0:-1] + fu + sp[8] + fu + sp[12] + fu + sp[9] + fu + sp[7] + fu + sp[-2])
    except:
        writetotxt('D:\data\AB\error',sp[0] + fu + sp[15] + fu + sp[4] + fu + sp[3] + fu + sp[-1][0:-1] + fu + sp[8] + fu + sp[12] + fu + sp[9] + fu + sp[7] + fu + sp[-2])

