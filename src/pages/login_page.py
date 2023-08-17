from selenium.webdriver.common.by import By

class LoginPage:

    username_txt = (By.XPATH, "//input[@name='username']")
    password_txt = (By.XPATH, "//input[@name='password']")   
    login_Btn = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        

        