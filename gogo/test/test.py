from flask import request,Blueprint
from flask_cors import CORS
from gogo.alltool import tryTool,Code
from gogo.heiheihei import logininto
import json


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
        if((b['user'] =="")&(b['password']=="")):
            raise tryTool.apiExceptionerror(Code.code.NULL_NAME)
        else:
            orture=logininto.intoandlogin.intoor(**b)
            if(orture==True):
                print(orture,"是否有信息")
                into=logininto.intoandlogin.intoor(**b)
                if(into==True):
                    print(orture,"是否注册成功")
                    raise tryTool.apiExceptionerror(Code.code.WIN_CODE)
            else:
                raise tryTool.apiExceptionerror(Code.code.REPEAT_NAME)

#登录接口 嘿嘿嘿
@user.route('/login',methods=['POST'])
def login():
        user = request.form.get("user");
        password = request.form.get("password");
        re=logininto.intoandlogin.loginyep(user,password)
        if(re==True):
            raise tryTool.apiExceptionerror(Code.code.WIN_CODE)
        else:
            raise tryTool.apiExceptionerror(Code.code.NO_INTOLOGIN)





