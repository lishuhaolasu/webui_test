import os
import time
from decimal import Decimal

import pyautogui
import pyperclip
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.remote.webelement import WebElement 

from common_utils.getlogger import logger
from common_utils.pathconf import SCREENSHOTS_DIR
from common_utils import conf

__all__ = ['BasePage']
class BasePage:
    def __init__(self, driver:Chrome):
        self.driver = driver
        self.ac = AC(self.driver)
        self.ww = WW(self.driver,
        timeout=int(conf.get('common','driver_timeout')),
        poll_frequency= float(conf.get('common','driver_frequency'))
        )
    def save_screenshot(self, name):
        filename = os.path.join(
            SCREENSHOTS_DIR, f'screenshot_{name}_{int(time.time())}.png')
        self.driver.save_screenshot(filename=filename)

    def find_element(self, locator: (str, str)) -> WebElement:
        if len(locator) > 2:
            addition_info = locator[2:]
            locator = locator[:2]
        else:
            addition_info = ["NOTHING"]
        if addition_info[0] == 'WAIT_FOR_VISIBLE':
            self.ww.until(EC.visibility_of_element_located(locator))
        elif addition_info[0] == 'WAIT_FOR_CLICKABLE':
            self.ww.until(EC.element_to_be_clickable(locator))
        try:
            e = self.driver.find_element(*locator)
            
            return e
        except NoSuchElementException as e:
            logger.exception(e)
            self.save_screenshot('find_element')
            raise e
        return None

    def find_elements(self, locator: (str,str)) -> [WebElement,]:
        try:
            el = self.driver.find_elements(*locator)
            return el
        except NoSuchElementException as e:
            logger.exception(e)
            self.save_screenshot('find_element')
            raise e
        return None
        
    def send_keys(self, locator: (str, str), data: str) -> bool:
        try:
            if isinstance(locator,tuple):
                e = self.find_element(locator)
            else:
                e = locator
            e.send_keys(data)
            return True
        except NoSuchElementException as e:
            logger.exception(e)
            self.save_screenshot('send_keys')
            raise e
        return False

    def click(self, locator: (str, str)) -> bool:
        try:
            if isinstance(locator,tuple):
                e = self.find_element(locator)
            else :
                e = locator
            e.click()
            return True
        except NoSuchElementException as e:
            logger.exception(e)
            self.save_screenshot('click')
            raise e
        return False

    def selector(self, locator: (str, str), by: (str, str)) -> bool:
        try:
            e = self.find_element(locator)
            selector = Select(e)
            getattr(selector, f'select_by_{by[0]}')(by[1])
            return True
        except NoSuchElementException as e:
            logger.exception(e)
            self.save_screenshot('selector')
            raise e
        return False

    def switch_frame(self, locator: (str, str)) -> bool:
        try:
            e = self.find_element(locator)
            self.driver.switch_to.frame(e)
        except NoSuchElementException as e:
            logger.exception(e)
            self.save_screenshot('switch_frame')
            raise e

    def ac_utils(self, meth: str, locator: (str, str)) -> bool:
        try:
            e = self.find_element(locator)
            getattr(self.ac, meth)(e)
            self.ac.perform()
            return bool
        except NoSuchElementException as e:
            logger.exception(e)
            self.save_screenshot(meth)
            raise e
        return False

    def scroll_to_end(self) -> bool:
        try:
            self.driver.execute_script('window.scrollTo(0,100000)')
            return True
        except NoSuchElementException as e:
            logger.exception(e)
            self.save_screenshot('double_click')
            raise e
        return False

    def upload_file(self, locator: (str, str), filepath, isinput=False) -> bool:
        try:
            if isinput:
                self.send_keys(locator, filepath)
            else:
                pyperclip.copy(filepath)
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(2)
                pyautogui.press('enter', presses=2)
            return True
        except NoSuchElementException as e:
            logger.exception(e)
            self.save_screenshot('double_click')
            raise e
        return False
    
    def assertequal(self,this,other):
        try:
            assert this,other 
        except AssertionError as e :
            logger.exception(e)
            self.save_screenshot('assertequal')
            raise e
    
    def assertin(self,this,other):
        try:
            if isinstance(type(this),type(other)) or issubclass(type(this),type(other)):
                if other in this:
                    return True
                else:
                    raise AssertionError('value is not contains')
            else:
                raise AssertionError(f'type is not same,{type(this),type(other)}')
        except AssertionError as e :
            logger.exception(e)
            self.save_screenshot('assertin')
            raise e