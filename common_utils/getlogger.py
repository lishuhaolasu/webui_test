import os
import logging
import logging.handlers
import ctypes
import platform
from common_utils import conf
from common_utils import LOG_DIR

class DbgViewHandler(logging.Handler):
    '''
    用来创建输出日志到dbgview的handler
    '''
    def emit(self, record):
        OutputDebugString = ctypes.windll.kernel32.OutputDebugStringW
        OutputDebugString(self.format(record))

class HandleLog(object):
    @staticmethod
    def get_logger():
        logger = logging.getLogger(conf.get('log', 'name'))
        logfmt = logging.Formatter("LASU : %(asctime)s\t%(module)s-line:%(lineno)d\t%(levelname)s\t%(name)s\t%(message)s")
        logger.setLevel(conf.get("log", "level"))
        cosl = logging.StreamHandler()
        cosl.setLevel(conf.get('log', 'cosl_level'))
        cosl.setFormatter(logfmt)
        logger.addHandler(cosl)

        logfn = os.path.join(LOG_DIR,"log.log")
        if conf.getboolean('log','is_rotating') :
            logfd = logging.handlers.RotatingFileHandler(filename=logfn,mode='a',encoding='utf-8',maxBytes=2*1024*1024,backupCount=100) 
        else:
            logfd = logging.FileHandler(filename=logfn, encoding="utf8")
        logfd.setLevel(conf.get("log", 'fd_level'))
        logfd.setFormatter(logfmt)
        logger.addHandler(logfd)
        if platform.system().lower() == 'windows' and conf.getboolean('log','log_todbg'):
            dbgfd = DbgViewHandler()
            dbgfd.setLevel(conf.get('log','dbg_level'))
            dbgfd.setFormatter(logfmt)
            logger.addHandler(dbgfd)
        return logger

logger = HandleLog.get_logger()
