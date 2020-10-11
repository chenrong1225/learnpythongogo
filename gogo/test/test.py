from flask import Flask,views,request,Blueprint,jsonify,abort
from flask_cors import CORS
from gogo.all import errortool,tryTool,Code
from gogo.all.Code import code
import json
from enum import Enum

user=Blueprint('user',__name__)
CORS(user, resources=r"/*")
#test=logininto.intoandlogin()
#注册有判断重复
@user.route('/into',methods=['POST'])
def into():
        #user = request.form.get("user");
        #password = request.form.get("'password");
        a=json.dumps(request.form)
        b=json.loads(a) #处理成json
        print(b['user'])
        if((b['user'] =="")&(b['password']=="")):
            print(code.NULL_NAME)
            raise tryTool.apiException(return_code=code.NULL_NAME,status_code=400)
        else:
            orture=test.intoor(**b)
            if(orture['num']==0):
                msg={'code':'0000','msg':orture['msg']}
                return msg
            else:
                msg={'code':'0001','msg':orture['msg']}
                return msg

#登录接口 嘿嘿嘿
@user.route('/login',methods=['POST'])
def login():
        user = request.form.get("user");
        password = request.form.get("password");
        test=logininto.intoandlogin(user,password)
        re=test.loginyep()
        if(re==1):
         print("yep")
         msg={'code':'0000','msg':'成功'}
         return msg
        else:
         print("没有数据要注册")
         msg={'code':'0001','msg':'没有账号信息'}
         return msg





