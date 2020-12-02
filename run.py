from flask import Flask
import config

from gogo.test.test import user
from gogo.alltool import error

app=Flask(__name__)
app.config.from_object(config.testconfig)
app.register_blueprint(user,url_prefix='/user')
#app1.register_error_handler(Code.Enum,tryTool.handle_flask_error)
app.register_blueprint(error,url_prefix='/error')


if __name__ == '__main__':

    app.run()