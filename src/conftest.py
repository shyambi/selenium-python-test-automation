import pytest
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
from src.pages.login_page import LoginPage



@pytest.fixture(scope="function")
def setup_teardown(request):
    #filename = "C:/Users/www.abcom.in/vscode-workspace/test-project/logs/test_execution.log"
    #logging.basicConfig(filename="C:/Users/www.abcom.in/vscode-workspace/test-project/logs/test_execution.log")
    #logging.FileHandler(filename, mode='a', encoding=None, delay=False, errors=None)
    #logging.debug("Initialized the webdriver session")
    
    ## Chrome Broswer Initialization
    chrome_service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    ## FireFox Browser Initialization
    #driver = webdriver.Firefox()
    
    #logging.debug("Initialized the webdriver session")
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    logging.debug("Closing the driver session")
    driver.quit()