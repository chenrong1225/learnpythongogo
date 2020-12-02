class baseconfig(object):
    DEBUG=False

class testconfig(baseconfig):
    HOST='0.0.0.0'
    PORT=5000
    SECRET_KEY = 'chen'
    DEBUG = True