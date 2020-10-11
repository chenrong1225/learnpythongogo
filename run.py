from flask import Flask,request,render_template

from gogo.test.test import user

app1=Flask(__name__)
app1.register_blueprint(user,url_prefix='/user')


if __name__ == '__main__':
    app1.run(host="0.0.0.0",debug=True,port='5000')