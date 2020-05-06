import os
import time
from decimal import Decimal

import selenium.webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from case_pages.base_page import BasePage
from case_locators.chat_page import ChatPage as CP
from common_utils import conf

class ChatPage(BasePage):
    def open_to_chat(self):
        current_handles = self.driver.window_handles
        self.find_element(CP.classp_button).click()
        self.ww.until(EC.new_window_is_opened(current_handles))
        new_handles = self.driver.window_handles
        self.driver.switch_to.window(new_handles[-1])
    
    def search_user(self,username):
        e = self.find_element(CP.search_user)
        e.send_keys(username)
        e.send_keys(Keys.ENTER)
        self.find_elements(CP.user_list)[0].click()

    def send_msg(self,msg):
        self.find_element(CP.input_area).send_keys(msg)
        self.find_element(CP.input_submit).click()