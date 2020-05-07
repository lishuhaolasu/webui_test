import os
import time
from decimal import Decimal

import selenium.webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC

from case_locators.homework_page import HomeworkPage as HP
from case_pages.base_page import BasePage
from common_utils import conf


class HomeworkPage(BasePage):
    
    def update_upload(self):
        
        e = self.find_element(HP.update_upload)
        self.ac.move_to_element(e).perform()
        e.click()
        self.find_element(HP.update_comfirm).click()

    def remove_old(self):
        elist = self.find_elements(HP.remove_uploaded)
        for ele in elist :
            ele.click()
    
    def upload_homework(self,filepath):
        # self.find_element(HP.upload_button).click()
        self.upload_file(HP.upload_button,filepath,isinput=True)

    def leave_message(self,msg):
        self.find_element(HP.message_input).click()
        e = self.find_element(HP.message_save)
        e.clear()
        e.send_keys(msg)
        self.find_element(HP.submit_input).click()

    def comfirm_upload(self):
        try:
            self.ww.until_not(EC.presence_of_element_located(HP.uploading))
        except :
            pass    
        e = self.find_element(HP.submit_buttom)
        # self.ac.move_to_element(e).perform()
        e.click()
        # self.find_element(HP.success_notice).click()
        self.ac.click()
    def check_upload(self):
        return self.find_element(HP.uploaded)