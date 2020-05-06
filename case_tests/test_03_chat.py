import os
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from case_pages.login_page import LoginPage
from case_pages.main_page import MainPage 
from case_pages.homework_page import HomeworkPage 
from case_pages.chat_page import ChatPage
from common_utils.handleconfig import conf
from common_utils.pathconf import BINS_DIR, DATA_DIR
from common_utils.getlogger import logger
from common_utils import conf
from case_datas.chat import chat_success

class TestChat:
    @pytest.mark.smoke
    @pytest.mark.parametrize('test_info',chat_success)
    def test_chat_success(self,test_info,get_browser_cls):
        driver = get_browser_cls
        lp = LoginPage(driver)
        mp = MainPage(driver)
        cp = ChatPage(driver)
        lp.open_url()
        driver.maximize_window()
        lp.login(conf.get('common','user_id'),conf.get('common','user_pw'))
        mp.open_url()
        mp.join_course(test_info['course_code'])
        mp.open_url()
        cp.open_to_chat()
        cp.search_user(test_info['username'])
        cp.send_msg(test_info['msg'])