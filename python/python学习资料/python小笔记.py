###1.python 读入文件  read()、readline()、readlines()                                      #https://www.jianshu.com/p/d8168034917c
###AGAC track 比赛  

read()的利端：一次性独读出文件放在一个大字符串中，速度最快
    read()的弊端：文件过大的时候，占用内存会过大
    
readline()：逐行读取文本，结果是一个list
    占用内存小，逐行读取
    由于是逐行读取，速度比较慢

readlines()：
    一次性读取文本的所有内容，结果是一个list
    这种方法读取的文本内容，每行文本末尾都会带一个'\n'换行符 (可以使用L.rstrip('\n')去掉换行符）

小结：最优雅的方式是用with，还可以隐式的处理异常。最快的读取是xreadlines()

###2.str与repo()区别                                                                      #参考https://www.jianshu.com/p/2a41315ca47e
str() 与 repr() 的不同在于：
    str() 的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
    repr() 的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。
    
###3.json读入方式
    json.loads() 读入字符串
    json.load()  读入文件
    
###4.reduce()
    from functools import reduce
    def add(x,y):
        return x + y
    print (reduce(add, range(1, 101)))
  
###5.区间处理函数interval：
    from interval import Interval
    
eg1：interval 只能拼接相邻区间;类似bedtools merge                                 
from functools import reduce
from interval import Interval
def join(x,y):
    A=Interval(x[0][0],x[0][1])
    B=Interval(y[0][0], y[0][1])
    print(A.join(B))
A=[[1,2]]
B=[[2,5]]
join(A,B)

eg2: 判断哪些sent_span，在下一个列表里面没交集：
sent_span=[(0, 153),
 (154, 302),
 (303, 418),
 (419, 533),
 (534, 665),
 (666, 827),
 (828, 1036),
 (1037, 1197),
 (1198, 1343),
 (1344, 1630),
 (1631, 1767),
 (1768, 1905),
 (1906, 2080),
 (2081, 2242)]
denotation_span=[(0, 37),
 (71, 75),
 (86, 92),
 (93, 112),
 (154, 176),
 (303, 312),
 (344, 348),
 (369, 378),
 (1631, 1649),
 (1654, 1667),
 (1691, 1697),
 (1701, 1708),
 (1781, 1788),
 (1803, 1811),
 (1812, 1827),
 (1831, 1836)]
A=sent_span.copy()    ###采用列表remove 方法，一定要copy(),不然会index 报错
record=[]
for i in range(len(sent_span)):
    num = 0
    for den_start, den_end in denotation_span:
        if den_start >= sent_span[i][0] and den_end <= sent_span[i][1]:
            num += 1
            ###break
    if num>0:
        print(sent_span[i][0],sent_span[i][1],"number=",num)
        record.append((sent_span[i][0],sent_span[i][1]))
        A.remove((sent_span[i][0],sent_span[i][1]))
print("record:",record)
print("A:",A)
                                    
#####result：                                   
#0 153 number= 4
#154 302 number= 1
#303 418 number= 3
#1631 1767 number= 4
#1768 1905 number= 4
#record: [(0, 153), (154, 302), (303, 418), (1631, 1767), (1768, 1905)]
#A: [(419, 533), (534, 665), (666, 827), (828, 1036), (1037, 1197), (1198, 1343), (1344, 1630), (1906, 2080), (2081, 2242)]

                                    
###6 python两个 list 获取交集，并集，差集的方法      https://blog.csdn.net/u012412259/article/details/53175473
1. 获取两个list 的交集
>>>a=[2,3,4,5]
>>>b=[2,5,8]
>>>[for i in a if i not in b]
Out[78]: [3, 4]   
>>>set(a).intersection(set(b))
Out[80]: {2, 5}   
2.获取两个list 的并集
>>>set(a).union(set(b))
Out[81]: {2, 3, 4, 5, 8} 
3.获取两个 list 的差集                                 
>>>list(set(b).difference(set(a)))
Out[82]: [8]                                
                      
###7.1 filter(func,seq) 过滤seq里面序列，func函数返回值是True or False.filter返回值是iterater.   #https://mbd.baidu.com/newspage/data/landingshare?pageType=1&isBdboxFrom=1&context=%7B%22nid%22%3A%22news_9223914821840656006%22%2C%22sourceFrom%22%3A%22bjh%22%7D
>>>def is_odd(n):
        return n%2==1
>>>list(filter(is_odd,[1,2,3,4,5,56]))
                                    
>>>import math
>>>def is_sqr(x):
        return math.sqrt(x) % 2 ==0
>>>list(filter(is_sqr,range(1,101)))
Out[55]: [4, 16, 36, 64, 100]
###7.2 genetor 生成器    ;使用for 循环调用，或者next() 调用
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
gen=_odd_iter()
for i in range(5):
    print(next(gen))
