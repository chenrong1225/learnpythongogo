import pymysql

class sqldb:
    def __init__(self,loca,port,user,password,dbname,sql):
        self.loca=loca
        self.user=user
        self.password=password
        self.dbname=dbname
        self.port=port
        self.sql=sql

    def conn(self):
        connect=pymysql.Connect(
            host=self.loca,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.dbname,
            charset="utf-8"
        )
        return  connect

    def sel(self):
        connect=self.conn();
        sursor= connect.cursor();
        sursor.execute(self.sql)





    def iud(self):
        connect=self.conn();
        sursor= connect.cursor();
        sursor.execute(self.sql)
        connect.commit();
        print('已处理',sursor.rowcount,'条数据')

        