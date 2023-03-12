from behave import *
from features.orange_hrm_elements import OrangeHrmElements
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('Open the Orange HRM home Page')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


@when('Enter Username "{user}" Password "{psw}"')
def step_impl(context, user, psw):
    context.driver.find_element(By.XPATH, OrangeHrmElements.user_input_text_box_XPATH).send_keys(user)
    context.driver.find_element(By.XPATH, OrangeHrmElements.password_input_text_box_XPATH).send_keys(psw)


@when('Click On Login Button')
def step_impl(context):
    context.driver.find_element(By.XPATH, OrangeHrmElements.login_button_XPATH).click()

@then('User Must Successfully Login to the Dashboard page')
def step_impl(context):
    status = context.driver.find_element(By.XPATH, OrangeHrmElements.dash_board_statusbar_XPATh).text
    assert status == "Dashboard"
    
@then('User should not be login with invalid data')
def step_impl(context):
    status = context.driver.find_element(By.XPATH, OrangeHrmElements.Invalid_credential_msg_XPATH).text
    assert status == "Invalid credentials"

