import os 
import time
from decimal import Decimal

import selenium.webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

from common_utils import conf
from .base_page import BasePage 
from case_locators.login_page import LoginPage as LP
__all__ = ['LoginPage']

class LoginPage(BasePage):
    '''
    登陆页面
    '''
    def open_url(self):
        url = conf.get('common','url')
        path = conf.get('common','login_path')
        self.full_url = url+path
        self.driver.get(self.full_url)
        
    def login(self,user_id,user_pw):
        self.find_element(LP.login_url).click()
        self.find_element(LP.userid).send_keys(user_id)
        self.find_element(LP.password).send_keys(user_pw)
        self.find_element(LP.login_button).click()

    def login_ok(self):
        self.ww.until(EC.url_changes(self.full_url))
        return self.driver.current_url
    
    def login_failed(self):
        e = self.find_element(LP.error_locator)
        return e.text
