import time
import unittest
from selenium import webdriver
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from orange_HRM_project_2.pages.orange_hrm_page_login import PageLogin
from orange_HRM_project_2.pages.orange_pim_module import PimPage
from orange_HRM_project_2.pages.orange_hrm_web_elements import OrangeHrmElements


class PimTestPage(unittest.TestCase):
    driver = None
    cwd = os.getcwd()

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver = cls.driver
        invalid_login = PageLogin(driver)
        invalid_login.user_login("Admin", "admin123")

    def test_01_create_new_employee(self):  # Test Case ID TC_PIM_03
        driver = self.driver
        new_employee = PimPage(driver)
        new_employee.click_pim()
        first_name = "Mohamed"
        last_name = "Mujahith"
        new_employee.click_new_employee_add_button()
        new_employee.enter_employee_name(first_name, last_name)
        new_employee.click_save_button()
        time.sleep(8)
        new_employee.enter_driver_license("L12345678")
        new_employee.enter_license_expiry("2023-05-21")
        new_employee.enter_ssn_number("12345")
        new_employee.enter_sin_number("678910")
        new_employee.select_nationality("Indian")
        new_employee.select_marital_status("Married")
        new_employee.enter_date_of_brith("1994-05-23")
        new_employee.select_gender("Male")
        new_employee.click_save_button()
        employee_full_name = first_name + ' ' + last_name
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//div[@class ='orangehrm-edit-employee-name']"), employee_full_name))
        employee_element = driver.find_element(By.XPATH, "//div[@class ='orangehrm-edit-employee-name']").text
        assert employee_element == employee_full_name

    def test_02_validate_employee_list_page(self):  # Test Case ID TC_PIM_04
        driver = self.driver
        validate_employee_list = PimPage(driver)
        test_data = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration',
                     'Job', 'Salary', 'Tax Exemptions', 'Report-to', 'Qualifications', 'Memberships']
        validate_employee_list.validate_employee_list_page()
        assert validate_employee_list.present_elements.sort() == test_data.sort()

    def test_03_fill_out_personal_details_page(self):  # Test Case ID TC_PIM_05
        driver = self.driver
        screen_shot_path = '%s%s' % (self.cwd, '\\test_screen_shot\\test_case_id_TC_PIM_05.png')
        scroll_element = driver.find_element(By.XPATH, "//h6[text()='Personal Details']")
        personal_details_page = PimPage(driver)
        personal_details_page.select_blood_Type("A-")
        personal_details_page.click_edit_save_button()
        myaction = ActionChains(driver)
        myaction.scroll_to_element(scroll_element).perform()
        time.sleep(3)
        driver.save_screenshot(screen_shot_path)

    def test_04_fill_out_contact_details_page(self):  # Test Case ID TC_PIM_06
        driver = self.driver
        contact_details_page = PimPage(driver)
        contact_details_page.click_employee_contact_details()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//h6[text()='Contact Details']"), "Contact Details"))
        time.sleep(5)
        contact_details_page.enter_street_name("New Street")
        contact_details_page.enter_city_name("Chennai")
        contact_details_page.enter_state_province("TAMIL NADU")
        contact_details_page.enter_zipcode("600028")
        contact_details_page.select_country("India")
        contact_details_page.enter_home_phone("+01234567891")
        contact_details_page.enter_mobile_no("+911234567891")
        contact_details_page.enter_work_phone_no("+99958544756")
        contact_details_page.enter_work_email("mohamed@gmail.com")
        contact_details_page.click_save_button()
        screen_shot_path = '%s%s' % (self.cwd, '\\test_screen_shot\\test_case_id_TC_PIM_06.png')
        scroll_element = driver.find_element(By.XPATH, "//h6[text()='Contact Details']")
        myaction = ActionChains(driver)
        myaction.scroll_to_element(scroll_element).perform()
        time.sleep(3)
        driver.save_screenshot(screen_shot_path)

    def test_05_fill_out_emergency_contacts_details_page(self):  # Test Case ID TC_PIM_07
        driver = self.driver
        emergency_contacts_details = PimPage(driver)
        emergency_contacts_details.click_employee_emergency_contact_details()
        emergency_contacts_details.click_assigned_emergency_contacts()
        name = "Sahana"
        emergency_contacts_details.enter_relation_contact_name(name)
        emergency_contacts_details.enter_relationship_details("Wife")
        emergency_contacts_details.enter_mobile_no("+123456789")
        emergency_contacts_details.click_save_button()
        expect_result_text = driver.find_element(By.XPATH, "//div[@role='cell'][2]")
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH, "//div[@role='cell'][1]")))
        assert expect_result_text.text == name

    def test_06_fill_out_dependent_contacts_details_page(self):  # Test Case ID TC_PIM_08
        driver = self.driver
        dependent_contacts_details_page = PimPage(driver)
        dependent_contacts_details_page.click_employee_dependent_contact_details()
        dependent_contacts_details_page.click_assigned_dependent_contact()
        name = "Saja"
        dependent_contacts_details_page.enter_relation_contact_name(name)
        dependent_contacts_details_page.select_relationship_dropdown("Child")
        dependent_contacts_details_page.enter_date_of_brith("2020-05-22")
        dependent_contacts_details_page.click_save_button()
        expect_result_text = driver.find_element(By.XPATH, "//div[@role='cell'][2]")
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH, "//div[@role='cell'][1]")))
        assert expect_result_text.text == name

    def test_07_fill_out_employee_job_details_page(self):  # Test Case ID TC_PIM_09
        driver = self.driver
        employee_job_details_page = PimPage(driver)
        employee_job_details_page.click_employee_job_details()
        time.sleep(5)
        employee_job_details_page.enter_joint_date("2000-02-01")
        employee_job_details_page.select_job_title_dropdown("QA Lead")
        employee_job_details_page.select_job_category_dropdown("Professionals")
        employee_job_details_page.select_sub_unit_dropdown("Quality Assurance")
        employee_job_details_page.select_location_dropdown("New York Sales Office")
        employee_job_details_page.select_employment_status_dropdown("Full-Time Contract")
        employee_job_details_page.click_employee_contract_toggle_button()
        employee_job_details_page.enter_employee_contract_start_end_date("2022-01-01", "2023-01-01")
        employee_job_details_page.click_save_button()
        screen_shot_path = '%s%s' % (self.cwd, '\\test_screen_shot\\test_case_id_TC_PIM_09.png')
        scroll_element = driver.find_element(By.XPATH, "//h6[text()='Job Details']")
        myaction = ActionChains(driver)
        myaction.scroll_to_element(scroll_element).perform()
        time.sleep(5)
        driver.save_screenshot(screen_shot_path)

    def test_08_validate_employee_job_details_termination_page(self):  # Test Case ID TC_PIM_10
        driver = self.driver
        termination_and_activation_page = PimPage(driver)
        termination_and_activation_page.click_employee_termination_and_activation_button()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH, OrangeHrmElements.termination_date_XPATH)))
        termination_and_activation_page.enter_employee_termination_date("2023-01-01")
        termination_and_activation_page.select_employee_termination_reason_dropdown("Contract Not Renewed")
        termination_and_activation_page.click_employee_required_save()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, OrangeHrmElements.terminate_employment_and_activation_XPATH), "Activate Employment"))
        visible_activation_button = driver.find_element(By.XPATH, OrangeHrmElements.
                                                        terminate_employment_and_activation_XPATH).text

        assert visible_activation_button == "Activate Employment"

    def test_09_activation_employment_page(self):  # Test Case ID TC_PIM_11
        driver = self.driver
        activation_employment = PimPage(driver)
        activation_employment.click_employee_termination_and_activation_button()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, OrangeHrmElements.terminate_employment_and_activation_XPATH), "Terminate Employment"))
        visible_terminate_employment_button = driver.find_element(By.XPATH, OrangeHrmElements.
                                                                  terminate_employment_and_activation_XPATH).text
        assert visible_terminate_employment_button == "Terminate Employment"

    def test_10_validate_employee_salary_page(self):  # Test Case ID TC_PIM_12
        driver = self.driver
        employee_salary_page = PimPage(driver)
        employee_salary_page.click_employee_salary_component_tap()
        employee_salary_page.click_assigned_salary_component()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//h6[text()=' Add Salary Component ']"), "Add Salary Component"))
        employee_salary_page.enter_employee_salary_component("Basic")
        employee_salary_page.select_pay_grade_dropdown("Grade 4")
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH, OrangeHrmElements.employee_pay_frequency_dropdown_button_XPATH)))
        employee_salary_page.select_pay_frequency_dropdown("Monthly")
        employee_salary_page.select_currency_dropdown("United States Dollar")
        employee_salary_page.enter_employee_salary_amount("20000")
        employee_salary_page.click_direct_deposit_details_toggle_button()
        employee_salary_page.enter_bank_account_number("AC123456789")
        employee_salary_page.select_bank_account_type_dropdown("Savings")
        employee_salary_page.enter_bank_routing_number("123456789")
        employee_salary_page.enter_deposit_amount("20000")
        employee_salary_page.click_employee_required_save()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, OrangeHrmElements.visible_salary_component_XPATH), "Salary Component"))
        record_found = driver.find_element(By.XPATH, OrangeHrmElements.visible_salary_component_XPATH)
        assert record_found.text == "Salary Component"

    def test_11_validate_tax_exemptions_page(self):  # Test Case ID TC_PIM_13
        driver = self.driver
        tax_exemptions_page = PimPage(driver)
        tax_exemptions_page.click_employee_stax_exemptions_tap()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH, OrangeHrmElements.federal_income_tax_status_dropdown_button_XPATH)))
        tax_exemptions_page.select_federal_income_tax_status_dropdown("Married")
        tax_exemptions_page.select_state_income_tax_state_dropdown("Alaska")
        tax_exemptions_page.select_state_income_tax_status_dropdown("Married")
        tax_exemptions_page.select_state_income_tax_unemployment_state_dropdown("Alabama")
        tax_exemptions_page.select_state_income_tax_work_state_dropdown("Alabama")
        tax_exemptions_page.click_save_button()
        screen_shot_path = '%s%s' % (self.cwd, '\\test_screen_shot\\test_case_id_TC_PIM_13.png')
        scroll_element = driver.find_element(By.XPATH, "//h6[text()='Tax Exemptions']")
        myaction = ActionChains(driver)
        myaction.scroll_to_element(scroll_element).perform()
        time.sleep(5)
        driver.save_screenshot(screen_shot_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
