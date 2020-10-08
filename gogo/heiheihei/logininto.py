from gogo.all import sql
import time

class intoandlogin:
    def __init__(self,user,password):
        self.user=user
        self.password=password

    #注册
    def logins(self):
        if(self.user.isspace()& self.password.isspace()):
            print("数值错误")
            print(self.user +"  and  "+ self.password)
        else:
            timedate=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            sqlinto="INSERT INTO testtb(name,pass,createTime,updatetime,num) VALUES('%s','%s','%s','%s',%s)"% \
            (self.user,self.password,timedate,timedate,'NULL')
            db=sql.sqldb(sqlinto)
            db.iud();


    #查询用户名是否重复
    def intoor(self):
        if(self.user.isspace()& self.password.isspace()):
            print("数值错误")
            print(self.user +"  and  "+ self.password)
        else:
            sqlinto="SELECT * FROM testtb WHERE name='%s'"%(self.user)
            db=sql.sqldb(sqlinto)
            re=db.sel()

            print(re)
            if(len(re)==0):
                print("没有数据")
                return 0
            else:
                print("有数据")
                return 1

    #登录
    def loginyep(self):
        if(self.user.isspace()& self.password.isspace()):
            print("数值错误")
            print(self.user +"  and  "+ self.password)
        else:
            #print('ssss'+self.user)
            sqlinto="SELECT * FROM testtb WHERE name='%s' and pass='%s'"%(self.user,self.password)
            db=sql.sqldb(sqlinto)
            re=db.sel()
            if(len(re)==0):
                print("没有数据")
                return 0
            else:
                print("有数据")
                return 1


    #查询用户名  ，判断旧密码前端判断
    def updatepass(self):
        if(self.user.isspace()):
            print("措地")
        else:
            sqlinto="SELECT * FROM testtb WHERE name='%s'"%(self.user)
            db=sql.sqldb(sqlinto)
            re=db.sel();
            if(len(re)==0):
                print("没有这个用户")
            else:
                print("有这个用户哦")
                return re


     #修改
    def update(self):
        if(self.user.isspace()& self.password.isspace()):
            print("数值错误")
            print(self.user +"  and  "+ self.password)
        else:
            sql="update testtb SET pass='%s' WHERE name='%s'"%(self.user,self.password)
            db=sql.sqldb(sql)
            db.iud