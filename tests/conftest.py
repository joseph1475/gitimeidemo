import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = None

def pytest_addoption(parser):
    parser.addoption(
       "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--user_name", action="store"
    )
    parser.addoption(
        "--password", action="store"
    )
    parser.addoption(
        "--driverpath", action="store"
    )
    parser.addoption(
        "--excel_Location", action="store"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    driver_path = request.config.getoption("driverpath")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=driver_path)
    elif browser_name=="firefox":
        driver = webdriver.Firefox(executable_path=driver_path)
    elif browser_name =="InternetExplorer":
        driver = webdriver.Ie(executable_path=driver_path)
    else:
        print("Wrong argument")
        #firefox browser code
    driver.implicitly_wait(5)
    driver.get("http://intranet.sonimtech.com/")
    intranet_url = driver.current_url
    assert intranet_url == "http://intranet.sonimtech.com/"
    driver.maximize_window()
    username = request.config.getoption("user_name")
    userid = driver.find_element_by_id('edit-name').send_keys(username)
    password = request.config.getoption("password")
    pwd = driver.find_element_by_id('edit-pass').send_keys(password)

    excel_Location = request.config.getoption("excel_Location")
    request.cls.excel_Location = excel_Location
    request.cls.driver =driver
    yield
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
