import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 用例目录
CASE_DIR = os.path.join(BASE_DIR, 'case_tests')

# 用例数据
DATA_DIR = os.path.join(BASE_DIR, 'case_datas')

# 通用模块
UTIL_DIR = os.path.join(BASE_DIR, 'common_utils')

# 额外库
SITE_DIR = os.path.join(BASE_DIR, 'addition_library')

# 配置文件
CONF_DIR = os.path.join(BASE_DIR, 'configs')

# 日志目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 截图目录
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screenshots')

# 报告目录
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 二进制文件
BINS_DIR = os.path.join(BASE_DIR,'bins')

pl = [p for p in globals() if p.endswith('DIR')]
for p in pl :
    os.makedirs(p,exist_ok=True)