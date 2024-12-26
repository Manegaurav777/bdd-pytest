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




@when(u'click on TestLogin')
def step_impl(context):
    global hpage
    hpage=Homepage(context.driver)
    hpage.clickOn_loginPageButton()

@then(u'Enter login Credentials')
def step_impl(context):
    global lpage
    lpage=LoginPage(context.driver)
    usr=Readconfig.getUsername()
    pwd=Readconfig.getPassword()
    lpage.EnterUsername(usr)
    lpage.EnterPasswords(pwd)
    time.sleep(5)

@then(u'Click on Submit')
def step_impl(context):
    lpage.ClickOnSubmit()


@then(u'Verify Page Title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "Logged In Successfully | Practice Test Automation"
    if actual_title == expected_title:
        assert True
        context.driver.save_screenshot(".\\Screenshots\\"+"loginPage.png")
        allure.attach(context.driver.get_screenshot_as_png(),name="c2ta", attachment_type=AttachmentType.PNG)
    else:
        mylogger.info("didnt matched")
        assert False
    time.sleep(5)









