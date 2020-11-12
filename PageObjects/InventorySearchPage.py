from selenium.webdriver.common.by import By


class InventorySearchPage:
    ImeiSearch = (By.XPATH, "//input[@name ='title']")
    inventory_submitBtn = (By.XPATH, "//input[@type ='submit']")
    employee_name =(By.XPATH, "//tr[1]/td[2]")
    imeiNumber = (By.XPATH, "//tr[1]/td[1]/a")
    model_name = (By.XPATH, "//tr[1]/td[5]")
    status = (By.XPATH, "//tr[1]/td[6]")

    def __init__(self, driver):
        self.driver = driver

    def InventoryImeiSearch(self):
        return self.driver.find_element(*InventorySearchPage.ImeiSearch)
        #self.driver.find_element_by_xpath("//input[@name ='title']").send_keys(imei)

    def InventorySearch_submitBtn(self):
        return self.driver.find_element(*InventorySearchPage.inventory_submitBtn)
        #self.driver.find_element_by_xpath("//input[@type ='submit']").click()

    def InventorySearch_imeiNo(self):
        return self.driver.find_element(*InventorySearchPage.imeiNumber)
        #imeinumber = self.driver.find_element_by_xpath("//tr[1]/td[1]/a").text

    def InventorySearch_name(self):
        return self.driver.find_element(*InventorySearchPage.employee_name)
        #employee = self.driver.find_element_by_xpath("//tr[1]/td[2]").text

    def InventorySearch_modelName(self):
        return self.driver.find_element(*InventorySearchPage.model_name)
        #model = self.driver.find_element_by_xpath("//tr[1]/td[5]").text

    def InventorySearch_Status(self):
        return self.driver.find_element(*InventorySearchPage.status)