import time

from features.orange_hrm_elements import OrangeHrmElements
from selenium import webdriver
from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

search_box_text = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory",
                   "Maintenance", "Buzz"]
result_data = []


@when('Enter the value on admin search box')
def step_impl(context):
    for search_text in search_box_text:
        search_box = context.driver.find_element(By.XPATH, OrangeHrmElements.admin_search_input_box_XPATH)
        search_box.send_keys(search_text)
        result_text = context.driver.find_element(By.XPATH, "//span[contains(@class,'menu-item--name')]").text
        result_data.append(result_text)
        search_box.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)


@then('The user should be able to search the  admin page and the individual menu')
def step_impl(context):
    assert search_box_text == result_data

