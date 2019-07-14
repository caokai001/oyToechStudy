
## 2.log模块
```
import sys
import logging

LOGGING_FMT = "%(name)-20s %(levelname)-7s @ %(asctime)s: %(message)s"
LOGGING_DATE_FMT = "%m/%d/%y %H:%M:%S"

def get_logger(name, level=None):
    log = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter(fmt=LOGGING_FMT, datefmt=LOGGING_DATE_FMT))
    log.addHandler(handler)
    if level:
        log.setLevel(level)
    else:
        log.setLevel(logging.DEBUG)
    return log
log=get_logger("yes","INFO")
log.warning("hello")
```



## 1. 下载及其展示图片  
参考[HPO project](https://github.com/Nanguage/BioTMCourse/blob/master/HPO%20enrich/hpoea/utils/download.py)

```
url = "http://wx4.sinaimg.cn/large/d030806aly1fq1vn8j0ajj21ho28bduy.jpg"

rsp = requests.get(url, stream=True)
with open("1.jpg","wb") as f:
    for i in rsp.iter_content(chunk_size=1024):  # 边下载边存硬盘, chunk_size 可以自由调整为可以更好地适合您的用例的数字
        f.write(i)
from PIL import Image
img=Image.open("1.jpg")
img.show()

from IPython.display import Image
Image(url= "1.jpg")

```


## 1. 下载文件
```
import logging
import requests
import os
from tqdm import tqdm


DATA_DIR = os.path.join(os.path.expanduser("~"))
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



def download_file(url, file_name,file_dir):
    """Download file and save it."""
    logger.info("Download file from: {}".format(url))
    response = requests.get(url, stream=True)
    path=os.path.join(file_dir,file_name)
    with open(path, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    logger.info("Data download done, file saved to: {}".format(path))
    return path


##
DATA_DIR = os.path.join(os.path.expanduser("~"),r"Desktop\152\HPO")
print(DATA_DIR)
# such as HPO example
HPO_OBO_URL = "https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo"
download_file(HPO_OBO_URL,"hpo.txt",DATA_DIR)
```



