from flask import jsonify
from gogo.alltool.tryTool import apiExceptionerror
from gogo.alltool.Code import code
from . import error
import json

@error.app_errorhandler(apiExceptionerror)
def handle_flask_error(error):
    response=jsonify(error.to_dict())
    #response.status_code=int(error.status_code)
    return response


#error.register_error_handler(code.__name__,handle_flask_error)