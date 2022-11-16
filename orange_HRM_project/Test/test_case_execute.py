from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from orange_HRM_project.Pages.orange_HRM_PMI_module_page import PIM_module
from orange_HRM_project.Pages.orange_HRM_delete_page import delete_page
from orange_HRM_project.Pages.orange_HRM_employee_details_edit_page import Employee_details_edit

from orange_HRM_project.Pages.orange_HRM_page_login import Page_Login

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


class Test_case:
    login = Page_Login(driver)
    PIM = PIM_module(driver)
    employee_edit = Employee_details_edit(driver)
    employee_delete = delete_page(driver)

    def TC_Login_01(self):  # valid_login
        self.login.enter_username("Admin")
        self.login.enter_password("admin123")
        self.login.click_login_button()
        time.sleep(10)

    def TC_Login_02(self): # invalid_login
        self.login.enter_username("Admin")
        self.login.enter_password("admin")
        self.login.click_login_button()
        time.sleep(10)

    def TC_PIM_01(self):  # new_employee_add
        self.login.enter_username("Admin")
        self.login.enter_password("admin123")
        self.login.click_login_button()
        self.PIM.click_PIM_module()
        self.PIM.click_new_employee_add_button()
        self.PIM.enter_employee_first_name("MOHAMED")
        self. PIM.enter_employee_last_name("MUJAHITH")
        self.PIM.click_save_button()
        time.sleep(10)

    def TC_PIM_02(self):   # edit_exiting_employee details for add driver license details and select the gender
        self. login.enter_username("Admin")
        self.login.enter_password("admin123")
        self.login.click_login_button()
        self.PIM.click_PIM_module()
        self.employee_edit.employee_list()
        self.employee_edit.search_employee_id("0355")  # any exiting employee ID number
        self.employee_edit.click_search_button()
        self.employee_edit.edit_button()
        time.sleep(5)
        self.employee_edit.enter_driver_license("L51256")
        self.employee_edit.enter_license_expiry("2023-05-01")
        self.employee_edit.select_gender("Male")
        self.employee_edit.click_edit_save_button()
        time.sleep(10)

    def TC_PIM_03(self):  # delete_exiting_employee
        self.login.enter_username("Admin")
        self.login.enter_password("admin123")
        self.login.click_login_button()
        self.PIM.click_PIM_module()
        self.employee_edit.employee_list()
        self.employee_edit.search_employee_id("0355")
        self.employee_edit.click_search_button()
        time.sleep(3)
        self.employee_delete.click_delete_button()
        time.sleep(10)



test = Test_case()

