from ..constants import Code


class apiExceptionerror(Exception):
    status_code=400
    def __init__(self,massage,status_code=None,payload=None,data=None):
        #Exception.__init__(self)
        self.message=massage
        if status_code is not  None:
            self.status_code= Code[massage]
        self.payload=payload
        self.data=data
    #构造要返回的错误代码和信息的字典
    def to_dict(self):
        rv=dict(self.payload or ())
        if(self.message.value is not None):
            self.status_code=self.message.value
        rv['status_code']=self.status_code
        rv['message']= Code.code.J_MSG.value[self.message.name]
        if(self.data is not None):
            rv['data']=self.data
        return rv

