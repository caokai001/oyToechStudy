#链接：https://www.zhihu.com/question/60868436/answer/307219795
###对scrPath中文件进行随机抽取175个，到datPath中
###
###
import random
import os
import shutil

def random_copyfile(srcPath,dstPath,numfiles):
    name_list=list(os.path.join(srcPath,name) for name in os.listdir(srcPath))
    random_name_list=list(random.sample(name_list,numfiles))
    if not os.path.exists(dstPath):
        os.mkdir(dstPath)
    for oldname in random_name_list:
        shutil.copyfile(oldname,oldname.replace(srcPath, dstPath))

srcPath='/home/kcao/test/tmp/AGAC_training'         
dstPath = '/home/kcao/test/tmp/train_data'
random_copyfile(srcPath,dstPath,175)
