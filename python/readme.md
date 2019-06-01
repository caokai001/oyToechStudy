### 记录python 学习
>## 1.eval这个函数就是在返回，它觉得正确的那个值   
a,b=eval(input())

>## 2.list copy 方法
<br>
>从以上可以看出，使用 a[:], list(a), a*1, copy.copy(a)四种方式复制列表结果都可以得到一个新的列表，但是如果列表中含有列表，所有b, c, d, e四个新列表的子列表都是指引到同一个对象上。只有使用copy.deepcopy(a)方法得到的新列表f才是包括子列表在内的完全复制。
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
