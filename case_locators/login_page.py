from selenium.webdriver.common.by import By

__all__ = ['LoginPage']

class LoginPage:
    login_url = (By.XPATH,"//a[contains(text(),'账号登录')]")
    userid = (By.XPATH,"//input[@name='account']")
    password = (By.XPATH,"//input[@name='pass']")
    login_button = (By.XPATH,"//a[@class='btn-btn']",'WAIT_FOR_VISIBLE')
    error_locator = (By.XPATH,"//p[@class='error-tips']")