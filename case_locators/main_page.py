from selenium.webdriver.common.by import By

__all__ = ['MainPage']


class MainPage:
    join_class = (
        By.XPATH, "//div[contains(text(),'加入课程') and contains(@class,'ktcon1l')]")
    course_input = (
        By.XPATH, "//input[contains(@placeholder,'课程')]", 'WAIT_FOR_VISIBLE')
    # comfirm_join = (By.XPATH, "//div[contains(text(),'加入课程') and contains(@class,'chuangjiankctop')]", 'WAIT_FOR_VISIBLE')
    comfirm_join = (By.XPATH,"//a[contains(text(),'加入')]")
    skip_tutorial = (
        By.XPATH, "//a[contains(@class,'introjs-button') and contains(@class,'introjs-skipbutton')]", 'WAIT_FOR_VISIBLE')
    jump_to_class = (By.XPATH, "//a[@class='jumptoclass']", 'WAIT_FOR_VISIBLE')
    more_button = (
        By.XPATH, "//span[contains(text(),'更多')]", 'WAIT_FOR_VISIBLE')
    quit_course = (By.XPATH, "//*[@class='kdli3']", 'WAIT_FOR_VISIBLE')
    quit_pass = (By.XPATH, "//input[@type='password']", 'WAIT_FOR_VISIBLE')
    comfirm_quit = (
        By.XPATH, "//a[contains(@class,'btn btn-positive') and contains(text(),'退课')]", 'WAIT_FOR_VISIBLE')
    # joined_course = (By.ID,'error-tip')