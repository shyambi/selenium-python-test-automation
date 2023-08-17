import pytest, allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest_html
import logging
from selenium.webdriver.safari.service import Service
from src.pages.login_page import LoginPage
#from src.log_config import setup_logger, get_logger
import logging



# Get a logger for this module
#logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("setup_teardown")
class TestLogin:

#    def setup_class(self):
#       setup_logger()
#        self.logger = get_logger(__name__)
        
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        loginpage = LoginPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        #time.sleep(10)
        wait.until(expected_conditions.visibility_of_element_located(loginpage.username_txt))
        self.driver.find_element(*loginpage.username_txt).click()
        logging.info("Clicked on username textbox")
        self.driver.find_element(*loginpage.username_txt).send_keys("Admin")
        logging.info("Send keys username is done")
        self.driver.find_element(*loginpage.password_txt).click()
        self.driver.find_element(*loginpage.password_txt).send_keys("admin123")
        allure.attach(self.driver.get_screenshot_as_png(), name="LoginPageScreenshot", attachment_type=AttachmentType.PNG)
        self.driver.find_element(*loginpage.login_Btn).click()
        logging.info("Clicked on login button")
        
        time.sleep(10)
        logging.info("Test Passed")
        