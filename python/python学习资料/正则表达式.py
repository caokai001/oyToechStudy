###正则表达式1
##资料来源：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000
##https://cuiqingcai.com/977.html
1.re模块
有了准备知识，我们就可以在Python中使用正则表达式了。Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用"\"转义，所以要特别注意：
>>> s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'
因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
>>> s = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'

2.切分字符串
用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：
>>> 'a b   c'.split(' ')
['a', 'b', '', '', 'c']
>>> re.split(r'[\s\,\;]+', 'a,b;; c  d')
['a', 'b', 'c', 'd']


3.分组
 >>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
 >>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'

4.贪婪匹配
最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：
>>> re.match(r'^(\d+)(0*)$', '102300').groups()
('102300', '')

由于"\d+"采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
必须让"\d+"采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个"?"就可以让"\d+"采用非贪婪匹配：
>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')

5.编译
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2.用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')

###练习：
1.匹配邮箱地址
def is_valid_email(addr): 
     if re.match(r"^(.*?)[@#](\w+?).com$",addr): 
         print("ok") 
is_valid_email('someone@gmail.com')





###正则表达式2
re 模块的一般使用步骤如下：
    .使用 compile 函数将正则表达式的字符串形式编译为一个 Pattern 对象
    .通过 Pattern 对象提供的一系列方法对文本进行匹配查找，获得匹配结果（一个 Match 对象）：match对象有很多属性方法###https://cuiqingcai.com/977.html
    .最后使用 Match 对象提供的属性和方法获得信息，根据需要进行其他的操作
函数：
    compile 函数：用于编译正则表达式，生成一个 Pattern 对象。
                re.compile(pattern[, flag])
            eg:  pattern = re.compile(r'\d+')
    match 函数
            用于查找字符串的头部（也可以指定起始位置），它是一次匹配，只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果。
                match(string[, pos[, endpos]])
            eg： m = pattern.match('one12twothree34four')  ###None

    search 函数
            它也是一次匹配，只要找到了一个匹配的结果就返回.
                search(string[, pos[, endpos]])
            eg:  m = pattern.search('one12twothree34four')

    findall 函数
            搜索整个字符串，获得所有匹配的结果.返回列表
                findall(string[, pos[, endpos]])
            eg：  result2 = pattern.findall('one1two2three3four4', 0, 10)
    finditer 函数
            搜索整个字符串，获得所有匹配的结果.返回迭代器
            
            eg:     result_iter2 = pattern.finditer('one1two2three3four4', 0, 10)
        
        
    split 函数
            按照能够匹配的子串将字符串分割后.返回列表
            split(string[, maxsplit])
            eg:     p = re.compile(r'[\s\,\;]+')
                    print (p.split('a,b;; c   d'))

    sub 函数
            sub 方法用于替换，返回是字符串。
        import re
        p = re.compile(r'(\w+) (\w+)')
        s = 'hello 123, hello 456'
        def func(m):
            return 'hi' + ' ' + m.group(2)
        print p.sub(r'hello world', s)  # 使用 'hello world' 替换 'hello 123' 和 'hello 456'
        print p.sub(r'\2 \1', s)        # 引用分组
        print p.sub(func, s)
        print p.sub(func, s, 1) 
        
        ##结果：
        hello world, hello world
        123 hello, 456 hello
        hi 123, hi 456
        hi 123, hello 456
        
    subn 函数
        和sub类似，但是返回的结果是元组：(sub(),替换次数)




