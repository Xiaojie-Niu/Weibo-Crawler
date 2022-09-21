def to_sql(weibo_total,dbname):
    
    #写入数据库
    conn = pymysql.connect(user='spider',password='****',host='***.***.**.**',port=3306,database='spider',use_unicode=True,charset="utf8")
    cs = conn.cursor()

    #整理字典数据
    for i in range(len(weibo_total['微博用户'])):
        data = ''
        for k in weibo_total.keys():
            data = (data + '\'' + '{}' + '\'' + ',').format(weibo_total[k][i])
        #data = '\"'+ data[:-1] + '\"' 
        #SQL语句执行
        sql = ("""INSERT INTO %s VALUES (%s)""") % (dbname,data[:-1])
        cs.execute(sql)
    cs.execute("SELECT * FROM %s"%dbname)
    conn.commit()
    print(cs.fetchall())
    conn.close()
