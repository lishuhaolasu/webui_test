import os
import time
from decimal import Decimal

import selenium.webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from case_locators.course_page import CoursePage as CP
from case_pages.base_page import BasePage
from common_utils import conf

class CoursePage(BasePage):
    
    def change_banner(self):
        self.find_element(CP.homework_page).click()
    
    def change_to_homework(self):
        try:
            self.find_element(CP.upload_button).click()
        except NoSuchElementException  as e :
            if not 'Homework/handup/homeworkid' in self.driver.current_url:
                raise e
        except TimeoutException as e :
            if not 'Homework/handup/homeworkid' in self.driver.current_url:
                raise e
