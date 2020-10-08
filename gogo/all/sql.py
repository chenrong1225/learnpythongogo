import pymysql
import json

class sqldb:
    def __init__(self,sql):
       # self.loca=loca
        #self.user=user
        #self.password=password
        #self.dbname=dbname
        #self.port=port
        self.sql=sql

    def conn(self):
        connect=pymysql.connect("localhost","root","123456","test")
        #,charset="utf-8"
        return connect

#查方法
    def sel(self):
        results=""
        #connect=pymysql.Connect(self.loca,self.port,self.user,self.password,self.dbname)
        connect=self.conn();
        sursor= connect.cursor();
        try:
            sursor.execute(self.sql)
            results=sursor.fetchall()
        except:
            connect.rollback()
        connect.close()
        return results
        #return json.dumps(results,ensure_ascii=False)


#增删改方法
    def iud(self):
        connect=self.conn()
        sursor= connect.cursor()
        try:
            sursor.execute(self.sql)
            connect.commit()
            print(self.sql)
        except:
            connect.rollback()
        print('已处理',sursor.rowcount,'条数据')
        connect.close()


