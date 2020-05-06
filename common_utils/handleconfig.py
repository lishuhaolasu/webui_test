import os
from configparser import ConfigParser
from common_utils import CONF_DIR
__all__ = ['HandleConfig','conf']
class HandleConfig(ConfigParser):
    '''处理config的类'''
    def __init__(self, filename:str):
        # 调用父类的init方法
        super().__init__()
        self.__filename = filename
        self.read(self.__filename,encoding="utf8")

    def write_data(self, section:str, options:str, value:str) -> None:
        """写入数据的方法"""
        if not self.has_section(section):
            self.add_section(section)
        self.set(section, options, value)
        with open(self.__filename,'w',encoding='utf-8') as fp:
            self.write(fp=fp)
        
# if __name__ == "__main__":
conf = HandleConfig(os.path.join(CONF_DIR,"config.ini"))