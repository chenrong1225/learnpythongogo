from gogo.all.Code import code
from flask import Flask,jsonify
app=Flask(__name__)

class apiException(Exception):
    status_code=400

    def __init__(self,return_code=None,status_code=None,payload=None):
        Exception.__init__(self)
        self.return_code=return_code
        print("1"+self.return_code)
        if status_code is not  None:
            self.status_code=status_code
        self.payload=payload

    #构造要返回的错误代码和信息的字典
    def to_dict1(self):
        rv=dict(self.payload or ())
        rv['return_code']=self.return_code
        rv['message']=code.J_MSG[self.return_code]
        return rv


