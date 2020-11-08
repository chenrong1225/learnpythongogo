from flask import request,redirect
from gogo.alltool import tryTool,Code
from gogo.heiheihei import logininto
import json
from . import user

@user.route('/test')
def testjump():
    #通过函数名获取对应的url路径
    url=url_for('into')
    #重定向
    return redirect(url)


#注册有判断重复
@user.route('/into',methods=['POST'],name='te_te')
def into():
        #user = request.form.get("user");
        #password = request.form.get("'password");
        a=json.dumps(request.form)
        b=json.loads(a) #处理成json
        if((b['user'] =="")&(b['password']=="")):
            raise tryTool.apiExceptionerror(Code.code.NULL_NAME)
        else:
            orture=logininto.intoandlogin.intoor(**b)
            print(orture)
            if(orture==True):
                into=logininto.intoandlogin.register(**b)
                if(into!=True):
                    print(into,"是否注册成功")
                    raise tryTool.apiExceptionerror(Code.code.WIN_CODE,data=into)
            else:
                raise tryTool.apiExceptionerror(Code.code.REPEAT_NAME)



#登录接口  methods默认get
@user.route('/login',methods=['POST'])
def login():
        user = request.form.get("user");
        password = request.form.get("password");
        re=logininto.intoandlogin.loginyep(user,password)
        if(re!=False):
            print(re )
            raise tryTool.apiExceptionerror(Code.code.WIN_CODE,data=re)
        else:
            raise tryTool.apiExceptionerror(Code.code.NO_INTOLOGIN)





