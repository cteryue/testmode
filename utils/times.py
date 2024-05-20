import datetime
import time
from functools import wraps
from textwrap import wrap


def timestamp():
    """时间戳"""
    return time.time()

def dt_strftime(format = "%Y%m"):
    """获取当前事件并且格式化"""
    return datetime.datetime.now().strftime(format)

def sleep(seconds = 1.0):
    """睡眠时间，默认1s"""
    time.sleep(seconds)

def running_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = timestamp()
        res = func(*args,**kwargs)
        print("校验元素done！用时%.3f秒!" % (timestamp() - start))
        return res

if __name__ == '__main__':
    print(dt_strftime("%Y/%m/%d-%H:%M:%S"))