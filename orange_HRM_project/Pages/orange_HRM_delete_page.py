import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from orange_HRM_project.Pages.orange_HRM_web_elements import Orange_HRM_Elements


class delete_page:
    def __init__(self, driver):
        self.driver = driver

    def click_delete_button(self):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.employee_delete_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.yes_delete_button_XPATH).click()
