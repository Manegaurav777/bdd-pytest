from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:
    UsernameInputBox="//input[@id='username']"
    PassowrdInputBox="//input[@id='password']"
    SubmitButton="//button[@id='submit']"

    def __init__(self, driver):
        self.driver = driver

    def EnterUsername(self,Username):
        self.driver.find_element_by_xpath(self.UsernameInputBox).send_keys(Username)

    def EnterPasswords(self,Password):
        self.driver.find_element_by_xpath(self.PassowrdInputBox).send_keys(Password)

    def ClickOnSubmit(self):
        self.driver.find_element_by_xpath(self.SubmitButton).click()




