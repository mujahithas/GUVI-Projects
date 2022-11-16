import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from orange_HRM_project.Pages.orange_HRM_web_elements import Orange_HRM_Elements


class Employee_details_edit:
    def __init__(self, driver):
        self.driver = driver

    def employee_list(self):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.employee_list_XPATH).click()

    def search_employee_id(self, employee_id):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.employee_id_XPATH).send_keys(employee_id)
        time.sleep(3)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.employee_search_button_XPATH).click()

    def edit_button(self):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.employee_edit_button).click()

    def enter_driver_license(self, license_no):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.driver_license_no_XPATH).send_keys(license_no)

    def enter_license_expiry(self, expiry_date):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.license_expiry_XPATH).send_keys(expiry_date)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, Orange_HRM_Elements.gender_male_XPATH).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, Orange_HRM_Elements.gender_female_XPATH).click()

    def click_edit_save_button(self):
        self.driver.find_element(By.XPATH,Orange_HRM_Elements.employee_edit_save_button).click()




