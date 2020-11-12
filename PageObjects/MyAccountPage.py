from selenium.webdriver.common.by import By


class MyAccountPage:
    MyAccount_Btn = (By.CLASS_NAME,"menu-path-user")
    Inventorysearch_link = (By.LINK_TEXT,"Please use this.")

    def __init__(self, driver):
        self.driver = driver

    def MyAccountBtn(self):
        return self.driver.find_element(*MyAccountPage.MyAccount_Btn)
        #my_account = self.driver.find_element_by_class_name("menu-path-user").text

    def MyAccount_inventorylink(self):
        return self.driver.find_element(*MyAccountPage.Inventorysearch_link)
        #self.driver.find_element_by_link_text("Please use this.").click()