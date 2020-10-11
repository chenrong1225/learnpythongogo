from enum import Enum,unique

class code(Enum):
    #用户名存在
    J_MSG={}
    REPEAT_NAME='0001'
    J_MSG['REPEAT_NAME'] = '用户已经存在'
    #保存失败
    SQL_SAVE_LOST='0002'
    #成功
    WIN_CODE='0000'
    #查询失败
    SQL_SELECT_LOST='1003'
    #用户名或密码为空
    NULL_NAME='0004'
    J_MSG['NULL_NAME'] = '用户名或密码为空'