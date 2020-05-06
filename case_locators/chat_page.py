from selenium.webdriver.common.by import By

__all__ = ['ChatPage']

class ChatPage:
    classp_button = (By.XPATH,"//div[@class='privateLetter']/a")
    search_user = (By.XPATH,"//*[@type and contains(@placeholder,'搜索')]")
    user_list = (By.XPATH,'//dd')
    input_area = (By.XPATH,"//textarea[(@class)]")
    input_submit = (By.CSS_SELECTOR,".btn.btn-positive","WAIT_FOR_CLICKABLE")
    