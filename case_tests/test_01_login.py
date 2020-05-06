import os
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from case_pages.login_page import LoginPage
from common_utils.handleconfig import conf
from common_utils.pathconf import BINS_DIR, DATA_DIR
from common_utils.getlogger import logger
from case_pages.login_page import LoginPage
from case_datas.login import login_failed,login_success
class TestLogin:
    @pytest.mark.smoke
    @pytest.mark.parametrize('test_info',login_success)
    def test_login_ok(self,test_info,get_browser_func):
        driver = get_browser_func
        lp = LoginPage(driver)
        lp.open_url()
        lp.login(test_info['user_id'],test_info['user_pw'])
        lp.assertin(lp.login_ok(),test_info['expected'])
    @pytest.mark.parametrize('test_info',login_failed)
    def test_login_failed(self,test_info,get_browser_func):
        driver = get_browser_func
        lp = LoginPage(driver)
        lp.open_url()
        lp.login(test_info['user_id'],test_info['user_pw'])
        lp.assertin(lp.login_failed(),test_info['expected'])
