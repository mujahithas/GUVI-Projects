from selenium import webdriver
from selenium.webdriver.common.by import By

from orange_HRM_project.Pages.orange_HRM_web_elements import Orange_HRM_Elements


class PIM_module:

    def __init__(self, driver):
        self.driver = driver

    def click_PIM_module(self):
        self.driver.find_element(By.LINK_TEXT, Orange_HRM_Elements.PIM_module_link_text).click()

    def click_new_employee_add_button(self):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.new_employee_add_button_XPATH).click()

    def enter_employee_first_name(self, firstname):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.employee_first_name_XPATH).send_keys(firstname)

    def enter_employee_middle_name(self, middlename):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.employee_middle_name_XPATH).send_keys(middlename)

    def enter_employee_last_name(self, lastname):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.employee_last_name_XPATH).send_keys(lastname)

    def click_save_button(self):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.save_button_XPATH).click()












