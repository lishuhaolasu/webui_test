import os

# 项目目录路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例模块目录的路径
CASE_DIR = os.path.join(BASE_DIR, "testcases")

# 用例数据目录的路径
DATA_DIR = os.path.join(BASE_DIR, "data")

# 测试报告目录的路径
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# 配置文件目录的路径
CONF_DIR = os.path.join(BASE_DIR, "conf")

# 日志文件目录
LOG_DIR = os.path.join(BASE_DIR, "logs")

# 历史token存放位置
TOKEN_DIR = os.path.join(BASE_DIR,"tokens")

# 二进制文件位置
BINS_DIR = os.path.join(BASE_DIR,'bins')

# 截图位置
SCREENSHOTS_DIR = os.path.join(BASE_DIR,'screenshots')