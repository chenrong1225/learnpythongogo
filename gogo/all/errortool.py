from flask import jsonify,Flask
from gogo.all.tryTool import apiException



app=Flask(__name__)

@app.errorhandler(apiException)
def handle_flask_error(error):
    response=jsonify((error.to_dict1()))
    response.status_code=error.status_code
    return response