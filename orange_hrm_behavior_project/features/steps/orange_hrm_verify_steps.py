import time

from features.orange_hrm_elements import OrangeHrmElements
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By


@given('launch browser for chrome')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@when('open the browser launch the orange HRM website')
def open_browser(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


@then('verify the logo has present')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, OrangeHrmElements.login_text_present_XPATH).text
    assert status == "Login"


@then('close the browser')
def close_browser(context):
    context.driver.close()
