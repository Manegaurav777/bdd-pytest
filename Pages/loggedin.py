from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Homepage:
    LoginPage_link = "//a[normalize-space()='Test Login Page']"

    def __init__(self, driver):
        self.driver = driver

    def clickOn_loginPageButton(self):
        self.driver.find_element_by_xpath(self.LoginPage_link).click()






