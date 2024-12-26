import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.HomePage import Homepage
from Pages.LoginPage import LoginPage
from Utilities.Logger import LogGen
from Utilities.Readproperties import Readconfig
import time

baseUrl = Readconfig.getLoginUrl()
mylogger = LogGen.loggen()


@given(u'Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    mylogger.info("driver initalised")
    context.driver.get(baseUrl)
    mylogger.info("browser Lanuched")


@then(u'Verify homepage title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "Test Login | Practice Test Automation"
    if actual_title == expected_title:
        assert True
        context.driver.save_screenshot(".\\Screenshots\\" + "loginPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="c2ta", attachment_type=AttachmentType.PNG)
    else:
        mylogger.info("didnt matched")
        assert False
    time.sleep(5)

@then(u'Close the browser')
def step_impl(context):
    context.driver.close()
    mylogger.info("driver is closed")
    mylogger.info("hello")
    mylogger.info("Good afternoon")
    mylogger.info("how are you")
    mylogger.info("how are you")



