### 记录python 学习

>[python3 文档](https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p11_add_logging_to_simple_scripts.html)
>## 1.eval这个函数就是在返回，它觉得正确的那个值   
a,b=eval(input())

>## 2.list copy 方法

>从以上可以看出，使用 a[:], list(a), a*1, copy.copy(a)四种方式复制列表结果都可以得到一个新的列表，但是如果列表中含有列表，所有b, c, d, e四个新列表的子列表都是指引到同一个对象上。只有使用`copy.deepcopy(a)`方法得到的新列表f才是包括子列表在内的完全复制。

```
import copy
a = [[10], 20]
b = a[:]
c = list(a)
d = a * 1
e = copy.copy(a)
f = copy.deepcopy(a)
a.append(21)
a[0].append(11)
print (id(a), a)
#[[10, 11], 20, 21]
print (id(b), b)
#[[10, 11], 20]
print (id(c), c)
#[[10, 11], 20]
print (id(d), d)
#[[10, 11], 20]
print (id(e), e)
#[[10, 11], 20]
print (id(f), f)
#[[10], 20]
```

##3.logging 模块
[参考](https://blog.csdn.net/huilan_same/article/details/77869225)
```
import logging
logger = logging.getLogger('test')
logging.basicConfig()  # basicConfig是logging提供的简单的配置方法，不用basicConfig则需要手动添加handler
logger.setLevel(logging.INFO)  # 输出所有大于等于INFO级别的log
logger.info('I am <info> message.')
logger.debug('I am <debug> message.')  # 不输出

```

##4.[python寻找list中最大值、最小值并返回其所在位置](https://blog.csdn.net/fengjiexyb/article/details/77435676)

c = [-10,-5,0,5,3,10,15,-20,25]

print(c.index(min(c)))  # 返回最小值
print(c.index(max(c))) # 返回最大值
