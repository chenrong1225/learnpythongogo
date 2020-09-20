maxnub=9;

def inp():
    num=0
    num =int(input("输入的要是数字哦："))
    return num


def turn(maxnum, num):
    while maxnum!=num :
        if(maxnum>num):
            if(maxnub-num>3):
              print("差距有点大你重新说吧")
              num=inp()
              continue
            else:
                print("你再猜猜")
                num=inp()

                continue
        else:
            print("你再猜猜吧")
            num=inp()
            continue
    else:
        print("一样的")


if __name__ == '__main__':
    num=inp()
    turn(maxnub,num)