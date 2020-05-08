import os
import time
import pytest
from common_utils.path_lib import CASE_DIR, REPORT_DIR
from common_utils import getdatepath

if __name__ == '__main__':
    # date_now = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
    # full_report_filename = getdatepath(prefix=REPORT_DIR,filename=f'report-{date_now}.html')
    pytest.main(['--reruns','3',f'--alluredir={REPORT_DIR}/'])



    