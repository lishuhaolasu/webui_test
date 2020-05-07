"""conftest.py 文件名称是固定的。

统一存放 fixture 的地方。
"""
import os
import time
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common_utils import conf
from common_utils.pathconf import BINS_DIR

@pytest.fixture(scope='class')
def get_browser_cls():
        opt = Options()
        if sys.platform == 'win32':
            driver_path = f'chromedriver_{conf.get("common","driver_version")}.exe'
        elif sys.platform == 'linux':
            driver_path = f'chromedriver_{conf.get("common","driver_version")}'
            opt.binary_location = '/usr/bin/chromium-browser'
            opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        opt.add_argument('window-size=1920x1080')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--hide-scrollbars')
        opt.add_argument('blink-settings=imagesEnabled=false')
        opt.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
        driver = webdriver.Chrome(executable_path=os.path.join(BINS_DIR, driver_path),chrome_options=opt)
        wait_timeout = int(conf.get('common', 'driver_timeout'))
        driver.implicitly_wait(wait_timeout)
        yield driver
        # time.sleep(10000)
        driver.quit()
@pytest.fixture(scope='function')
def get_browser_func():
        opt = Options()
        if sys.platform == 'win32':
            driver_path = f'chromedriver_{conf.get("common","driver_version")}.exe'
        elif sys.platform == 'linux':
            driver_path = f'chromedriver_{conf.get("common","driver_version")}'
            opt.binary_location = '/usr/bin/chromium-browser'
            opt.add_argument('--headless')
        opt.add_argument('--no-sandbox')
        opt.add_argument('window-size=1920x1080')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--hide-scrollbars')
        opt.add_argument('blink-settings=imagesEnabled=false')
        opt.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
        driver = webdriver.Chrome(executable_path=os.path.join(BINS_DIR, driver_path),chrome_options=opt)
        wait_timeout = int(conf.get('common', 'driver_timeout'))
        driver.implicitly_wait(wait_timeout)
        yield driver
        # time.sleep(30)
        driver.quit()