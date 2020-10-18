import time
from gogo.alltool import sql


class intoandlogin:


    #注册
    def logins(**map):
            timedate=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            sqlinto="INSERT INTO testtb(name,pass,createTime,updatetime,num) VALUES('%s','%s','%s','%s',%s)"% \
            (map['user'],map['password'],timedate,timedate,'NULL')
            print(map['name'],"aaa",map['password'])
            db=sql.sqldb(sqlinto)
            cou=db.iud();
            if(len(cou)==0):
                return False
            else:
                return True


    #查询用户名是否重复,返回true可以注册，返回false不能注册
    def intoor(**map):
            sqlinto="SELECT * FROM testtb WHERE name='%s'"%(map.get('user') )
            db=sql.sqldb(sqlinto)
            re=db.sel()
            print(re)
            if(len(re)==0):
                print("没有数据")
                return  True
            else:
                print("有数据")
                return False

    #登录，返回False没有数据无法登陆，返回true可以登陆
    def loginyep(user,password):
            #print('ssss'+self.user)
            sqlinto="SELECT * FROM testtb WHERE name='%s' and pass='%s'"%(user,password)
            db=sql.sqldb(sqlinto)
            re=db.sel()
            if(len(re)==0):
                print("没有数据")
                return False
            else:
                print("有数据")
                return True


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
            sql="update testtb SET pass='%s' and updatetime='%s' WHERE name='%s'"%(self.user,self.updatetime,self.password)
            db=sql.sqldb(sql)
            db.iud