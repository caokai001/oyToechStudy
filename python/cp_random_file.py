#链接：https://www.zhihu.com/question/60868436/answer/307219795
###对scrPath中250文件进行随机抽取175个，到datPath中
###
###
import random
import os
import shutil

def random_copyfile(srcPath,dstPath,lastpath,numfiles):
    name_list=list(os.path.join(srcPath,name) for name in os.listdir(srcPath))
    random_name_list=list(random.sample(name_list,numfiles))
    last=[ item for item in name_list if item not in random_name_list ]
    if not os.path.exists(dstPath):
        os.mkdir(dstPath)
    for oldname in random_name_list:
        shutil.copyfile(oldname,oldname.replace(srcPath, dstPath))
    for file in last:
        shutil.copyfile(file,file.replace(srcPath, lastpath))

srcPath='/home/kcao/test/tmp/AGAC_training'
dstPath = '/home/kcao/test/tmp/kcao_train_data'
lastpath='/home/kcao/test/tmp/kcao_test_data'
random_copyfile(srcPath,dstPath,lastpath,175)



------------------------------------------------------------------------------------------------------------------------------------------
###知识点总结：
#1.通常习惯的写法，合并目录
>>> import os
>>> os.path.join('/hello/','good/boy/','doiido')
输出：'/hello/good/boy/doiido'

#2.os.listdir()
#3.shutil
#是一种高层次的文件操作工具
#类似于高级API，而且主要强大之处在于其对文件的复制与删除操作更是比较支持好。
#参考：https://www.jianshu.com/p/b4c87aa6fd24
shutil.mv文件移动
>>>shutil.move('C:/Users/xiaoxinsoso/Desktop/aaa', 'C:/Users/xiaoxinsoso/Desktop/bbb') # 把aaa目录移动到bbb目录下
