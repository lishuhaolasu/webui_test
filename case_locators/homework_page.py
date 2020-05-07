from selenium.webdriver.common.by import By

__all__ = ['HomeworkPage']


class HomeworkPage:
    upload_button = (By.XPATH,"//input[@name='file']")
    # upload_button = (By.CSS_SELECTOR, '.sc-btn.webuploader-container')
    message_input = (By.XPATH, "//span[@class='s2']")
    message_save = (By.ID,'comment')
    submit_input = (
        By.XPATH, "//a[contains(@class,'sure active') and contains(text(),'保存')]")
    submit_buttom = (By.CSS_SELECTOR, ".new-tj2",'WAIT_FOR_CLICKABLE')
    uploading = (By.CLASS_NAME,'ing')
    success_notice = (
        By.XPATH, "//a[contains(@class,'weui_btn_dialog primary')]", "WAIT_FOR_VISIBLE")
    update_upload = (By.XPATH,"//a[@class='new-tj1']")
    update_comfirm = (By.XPATH,"//a[contains(@class,'sure active') and contains(text(),'确定')]")
    remove_uploaded = (By.XPATH,"//a[contains(@class,'cancel hide')]")
    uploaded = (By.CSS_SELECTOR,'.ywc"]')