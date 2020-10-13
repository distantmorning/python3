import pymysql

#操作mysql数据库
#插入功能

db = pymysql.connect(host='134.175.198.59', user='zkhb', password='zkhb', port=3306, db='ehdata')
cursor = db.cursor()
user = 'tgtg'
sql = 'INSERT INTO inori(name) values(%s)'
try:
    cursor.execute(sql, (user))
    db.commit()
except:
    db.rollback()
db.close()
