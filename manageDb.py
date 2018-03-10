from pymysql import *


def connectTest(host, port, username, pwd):
    port = int(port)
    try:
        conn = connect(host=host, port=port, user=username, password=pwd)
        return True
    except BaseException as e:
        print(e)
        return False
