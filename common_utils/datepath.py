import os
import datetime 
import time
def main(prefix=None,filename=None) -> str:
    datenow = datetime.datetime.fromtimestamp(time.time())
    subpath = '{0}\\{0}{1}\\{0}{1}{2}'.format(datenow.year,datenow.month,datenow.day)
    if not prefix:
        fullpath = subpath
    else:
        fullpath = os.path.join(prefix,subpath)
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)
    if not filename:
        return fullpath
    else:
        return os.path.join(fullpath,filename)