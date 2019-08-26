source:  https://github.com/mgss/python-demo


# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:42:52 2019

@author: 16926
"""
#Demo-1
L=[11,22,33,44,55,66,77,88,99,90]
{"k1":list(filter(lambda x:x>66,L)),"k2":list(filter(lambda x:x<66,L))}

#Demo-2
from typing import Iterable,List,Tuple,Dict
import logging
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

def remove_strip(x:Iterable):
    '''
    input different data structure
    '''
    if isinstance(x,List):
        return list(map(str.strip,li))
    elif isinstance(x,Tuple):
        return tuple(map(str.strip,li))
    elif isinstance(x,Dict):
        return dict(map(str.strip,li))
    else:
        logging.warning("notice input data structure")


def p(x:Iterable):
    return list(filter(lambda item:item.endswith('c') and item.capitalize().startswith('A'),x))

def main(x:Iterable):
    if isinstance(x,Dict):
        return p(x.values())
    else:
        return p(x)
if __name__=="__main__":
    print(main(li))
    print(remove_strip(li))
        
#Demo-3
li = ["手机", "电脑", '鼠标垫', '游艇']
for index, text in enumerate(li,1):
    print(index, text)

inp = input("请选择要购买的商品：")
inp_num = int(inp)
print(li[inp_num-1])

#Demo-10
f=lambda i:True if i == None or i.isspace() == True or i == '' else False
if any(map(f,li))==True:
    print("有空内容")

#Demo-9
def is_length(obj):
    obj_len = 0
    for i in obj:
        obj_len += 1
    if obj_len > 5:
        print(obj, "长度大于5")
    else:
        print(obj, "长度为", obj_len)

#Demo-22
import logging

logging.basicConfig(
    #filename="base.log",
    format="[%(lineno)d]%(asctime)s - %(pathname)s - %(levelname)-8s - %(module)s : %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10, 'log')

#Demo-19
import sys
import time

for i in range(101):
    # 清除屏幕
    sys.stdout.write("\r")

    # 显示百分比和进度条
    sys.stdout.write("[%s%%|%-100s]" % (i, i * ('█')))

    # 从缓存刷入到屏幕
    sys.stdout.flush()

    # 延时0.3秒
    time.sleep(0.3)


#Demo-16
import time
def decorator_2(func):
    """
    最外层装饰器
    :param func:
    :return:
    """
    def warp(*args, **kwargs):
        print("最外层装饰器1".center(20, "="))
        ret = func(*args, **kwargs)
        print("最外层装饰器2".center(20, "="))
        return ret

    return warp
@decorator_2
def s(x:int)->int:
    '''
    :param x : number
    :return :
    '''
    return x*2

print(s(5))

#Demo-14
import random

code = ""
for i in range(4):

    num = random.randrange(0, 2)

    # 当前位显示字母或者数字各有50%几率
    if num == 0:
        # 随机显示数字
        r1 = random.randrange(0, 10)
        code += str(r1)
    else:
        # 随机显示字母
        i = random.randrange(65, 91)
        c = chr(i)
        code += c

print(code)

#Demo-25 并行运行
import psutil
from math import sqrt
%timeit [sqrt(i ** 2) for i in range(1000)]

#
print("CPU number :{}".format(psutil.cpu_count()))
from joblib import Parallel, delayed
%timeit Parallel(n_jobs=2)(delayed(sqrt)(i ** 2) for i in range(1000))



