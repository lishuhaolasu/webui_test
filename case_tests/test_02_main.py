import os
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from case_pages.login_page import LoginPage
from case_pages.main_page import MainPage 
from case_pages.homework_page import HomeworkPage 
from case_pages.course_page import CoursePage
from common_utils.handleconfig import conf
from common_utils.pathconf import BINS_DIR, DATA_DIR
from common_utils.getlogger import logger
from common_utils import conf
from case_datas.homework import upload_success
class TestMain:
    @pytest.mark.smoke
    @pytest.mark.parametrize('test_info',upload_success)
    def test_homework_success(self,test_info,get_browser_cls):
        driver = get_browser_cls
        lp = LoginPage(driver)
        mp = MainPage(driver)
        hp = HomeworkPage(driver)
        cp = CoursePage(driver)
        lp.open_url()
        driver.maximize_window()
        lp.login(conf.get('common','user_id'),conf.get('common','user_pw'))
        mp.open_url()
        # time.sleep(10)
        mp.join_course(test_info['course_code'])
        mp.jump_to_class()
        cp.change_banner()
        cp.driver.refresh()
        cp.change_to_homework()
        hp.update_upload()
        hp.remove_old()
        hp.upload_homework(test_info['filepath'])
        hp.leave_message(test_info['msg'])
        hp.comfirm_upload()
        driver.refresh()
        mp.open_url()
        mp.quit_class()
