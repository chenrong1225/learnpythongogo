from flask import Flask,request,render_template,current_app
from gogo.alltool import tryTool,Code,errortool
from gogo.test import user
from gogo.alltool import error
import config2

#__name__表示当前模块名字,static为静态目录，templates为模板目录
app1=Flask(__name__,static_url_path='/static')

app1.register_blueprint(user,url_prefix='/user')
app1.register_blueprint(error,url_prefix='/error')

#配置参数方式
#1.使用配置文件
#app1.config.from_pyfile("config.cfg")
#2.使用对象配置
app1.config.from_object(config2.config)
#3.直接设置
#app1.config['DEBUG']=True

#读取配置
#1.直接从app.config.get得到
#app1.config.get('CESHI')
#2.通过current_app取值
current_app.config.get('DEBUG')

if __name__ == '__main__':
    app1.run(host="0.0.0.0",port='5000')