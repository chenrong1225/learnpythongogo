from gogo.heiheihei import logininto
from flask import Flask,views,request
from flask_cors import CORS
from gogo.all import sql

app = Flask(__name__)
CORS(app, resources=r"/*")

@app.route('/into',methods=['POST'])
def into():
    user = request.form.get("user");
    password = request.form.get("password");
    test=logininto.intoandlogin(user,password)
    orture=test.intoor()
    if(orture==1):
        msg={'code':'0001','msg':'用户名重复'}
        return msg
    else:
        test.logins()
        msg={'code':'0000','msg':'成功'}
        return msg

#登录接口 嘿嘿嘿
@app.route('/login',methods=['POST'])
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





if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port='5000')