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
#通常习惯的写法，合并目录
>>> import os
>>> os.path.join('/hello/','good/boy/','doiido')
输出：'/hello/good/boy/doiido'
