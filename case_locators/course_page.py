from selenium.webdriver.common.by import By

__all__ = ['CoursePage'] 

class CoursePage:
    homework_page = (By.XPATH,"//a[contains(text(),'作业')]","WAIT_FOR_CLICKABLE")
    upload_button = (By.XPATH,"//a[@class='view-work']", 'WAIT_FOR_CLICKABLE')
    

