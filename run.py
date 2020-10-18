from flask import Flask,request,render_template
from gogo.alltool import tryTool,Code,errortool

from gogo.test.test import user
from gogo.alltool import error

app1=Flask(__name__)
app1.register_blueprint(user,url_prefix='/user')
#app1.register_error_handler(Code.Enum,tryTool.handle_flask_error)
app1.register_blueprint(error,url_prefix='/error')


if __name__ == '__main__':
    app1.run(host="0.0.0.0",debug=True,port='5000')