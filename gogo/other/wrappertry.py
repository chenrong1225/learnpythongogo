import logging

def wrappers(func):
    def wrapper(*args,**kwargs):
        print("装饰器")
        return func(*args,**kwargs)
    return wrapper()

@wrappers
def testwrapper():
    print("testwrapper")




if __name__ == '__main__':
    testwrapper