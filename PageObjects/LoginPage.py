from selenium.webdriver.common.by import By


class LoginPage:
    userid = (By.ID, "edit-name")
    pwd = (By.ID, "edit-pass")
    captcha =(By.CLASS_NAME,"field-prefix")
    captcha_Response = (By.ID,"edit-captcha-response")
    submitBtn = (By.XPATH, "//input[@value ='Log in']")

    def __init__(self, driver):
        self.driver = driver

    def loginuserid(self):
        return self.driver.find_element(*LoginPage.userid)
        # driver.find_element_by_id('edit-name')

    def login_pwd(self):
        return self.driver.find_element_by_id(*LoginPage.pwd)
        #driver.find_element_by_id.send_keys("minu@1013")

    def login_captcha(self):
        return self.driver.find_element(*LoginPage.captcha)
        #captcha = self.driver.find_element_by_class_name("field-prefix").text

    def Login_captchaResponse(self):
        return self.driver.find_element(*LoginPage.captcha_Response)
        #self.driver.find_element_by_id('edit-captcha-response')

    def Login_submitBtn(self):
        return self.driver.find_element(*LoginPage.submitBtn)
    #self.driver.find_element_by_xpath("//input[@value ='Log in']").click()