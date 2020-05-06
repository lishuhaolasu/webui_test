
import time
from decimal import Decimal

import selenium.webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as WW

from case_locators.main_page import MainPage as MP
from case_pages.base_page import BasePage
from common_utils import conf

__all__ = ['MainPage']


class MainPage(BasePage):

    def open_url(self):
        url = conf.get('common', 'url')
        path = conf.get('common', 'home_path')
        self.full_url = url+path
        self.driver.get(self.full_url)

    def join_course(self, course_code=''):
        self.find_element(MP.join_class).click()
        self.find_element(MP.course_input).send_keys(course_code)
        self.find_element(MP.comfirm_join).click()

    def jump_to_class(self):
        self.find_element(MP.jump_to_class).click()

    def quit_class(self):
        self.find_element(MP.more_button).click()
        self.find_element(MP.quit_course).click()
        self.find_element(MP.quit_pass).send_keys(conf.get('common', 'user_pw'))
        self.find_element(MP.comfirm_quit).click()

    # def joined_course(self):
    #     try:
    #         self.find_element(MP.joined_course)
    #     except :
    #         pass