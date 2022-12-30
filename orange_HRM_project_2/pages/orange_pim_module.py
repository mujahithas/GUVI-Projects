from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from orange_HRM_project_2.pages.orange_hrm_web_elements import OrangeHrmElements


class PimPage:
    present_elements = []

    def __init__(self, driver):
        self.driver = driver

    def click_pim(self):
        self.driver.find_element(By.LINK_TEXT, OrangeHrmElements.PIM_module_link_text).click()

    def click_new_employee_add_button(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.new_employee_add_button_XPATH).click()

    def enter_employee_name(self, firstname, lastname):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_first_name_XPATH).send_keys(firstname)
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_last_name_XPATH).send_keys(lastname)

    def click_save_button(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.save_button_XPATH).click()

    def click_edit_save_button(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.edit_save_button).click()

    def enter_driver_license(self, license_no):
        self.driver.find_element(By.XPATH, OrangeHrmElements.driver_license_no_XPATH).send_keys(license_no)

    def enter_license_expiry(self, expiry_date):
        self.driver.find_element(By.XPATH, OrangeHrmElements.license_expiry_XPATH).send_keys(expiry_date)

    def enter_date_of_brith(self, date_of_brith):
        self.driver.find_element(By.XPATH, OrangeHrmElements.date_of_brith).send_keys(date_of_brith)

    def enter_ssn_number(self, ssn_number):
        self.driver.find_element(By.XPATH, OrangeHrmElements.SSN_number_XPATH).send_keys(ssn_number)

    def enter_sin_number(self, sin_number):
        self.driver.find_element(By.XPATH, OrangeHrmElements.SIN_number_XPATH).send_keys(sin_number)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, OrangeHrmElements.gender_male_XPATH).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, OrangeHrmElements.gender_female_XPATH).click()

    def select_marital_status(self, status):
        self.driver.find_element(By.XPATH, OrangeHrmElements.marital_status_button_XPATH).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, OrangeHrmElements.marital_status_list)))
        marital_status_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.marital_status_list)
        for marital_status in marital_status_list:
            if status == marital_status.text:
                marital_status.click()
                break

    def select_nationality(self, nation):
        self.driver.find_element(By.XPATH, OrangeHrmElements.nationality_button_XPATH).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, OrangeHrmElements.nationality_list)))
        nationalitylist = self.driver.find_elements(By.XPATH, OrangeHrmElements.nationality_list)
        for nationality in nationalitylist:
            if nation == nationality.text:
                nationality.click()
                break

    def employee_list(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_list_XPATH).click()

    def search_employee_id(self, employee_id):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_id_XPATH).send_keys(employee_id)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_search_button_XPATH).click()

    def enter_employee_full_name(self, full_name):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_full_name_XPATH).send_keys(full_name)

    def validate_employee_list_page(self):
        employee_element = self.driver.find_elements(By.XPATH, OrangeHrmElements.employee_list_present_elements_XPATH)
        for present_element in employee_element:
            self.present_elements.append(present_element.text)

    def select_blood_Type(self, blood):
        self.driver.find_element(By.XPATH, OrangeHrmElements.blood_type_button_XPATH).click()
        blood_type_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.blood_type_list_XPATH)
        for blood_list in blood_type_list:
            if blood == blood_list.text:
                blood_list.click()
                break

    def click_employee_contact_details(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_contact_details_tap_XPATH).click()

    def enter_street_name(self, street):
        self.driver.find_element(By.XPATH, OrangeHrmElements.street_1_input_box_XPATH).send_keys(street)

    def enter_city_name(self, city):
        self.driver.find_element(By.XPATH, OrangeHrmElements.city_input_box_XPATH).send_keys(city)

    def enter_state_province(self, state):
        self.driver.find_element(By.XPATH, OrangeHrmElements.state_province_input_box_XPATH).send_keys(state)

    def enter_zipcode(self, zipcode):
        self.driver.find_element(By.XPATH, OrangeHrmElements.zip_code_input_box_XPATH).send_keys(zipcode)

    def select_country(self, country):
        self.driver.find_element(By.XPATH, OrangeHrmElements.country_button_XPATH).click()
        country_type_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.country_type_list_XPATH)
        for country_list in country_type_list:
            if country == country_list.text:
                country_list.click()
                break

    def enter_home_phone(self, phone):
        self.driver.find_element(By.XPATH, OrangeHrmElements.home_phone_no_XPATH).send_keys(phone)

    def enter_mobile_no(self, mobile):
        self.driver.find_element(By.XPATH, OrangeHrmElements.mobile_no_XPATH).send_keys(mobile)

    def enter_work_phone_no(self, phone):
        self.driver.find_element(By.XPATH, OrangeHrmElements.work_phone_no_XPATH).send_keys(phone)

    def enter_work_email(self, mail):
        self.driver.find_element(By.XPATH, OrangeHrmElements.work_email_id_XPATH).send_keys(mail)

    def click_employee_emergency_contact_details(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_emergency_contact_details_tap_XPATH).click()

    def click_assigned_emergency_contacts(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.emergency_contacts_add_button_XPATH).click()

    def enter_relation_contact_name(self, name):
        self.driver.find_element(By.XPATH, OrangeHrmElements.emergency_contacts_name_input_XPATH).send_keys(name)

    def enter_relationship_details(self, relationship):
        self.driver.find_element(By.XPATH, OrangeHrmElements.relationship_input_XPATH).send_keys(relationship)

    def select_relationship_dropdown(self, relation):
        self.driver.find_element(By.XPATH, OrangeHrmElements.relationship_dropdown_button_XPATH).click()
        relationship_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.blood_type_list_XPATH)
        for relation_list in relationship_list:
            if relation == relation_list.text:
                relation_list.click()
                break

    def click_employee_dependent_contact_details(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_dependent_contact_details_tap_XPATH).click()

    def click_assigned_dependent_contact(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_dependent_add_button_XPATH).click()

    def enter_joint_date(self, join_date):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_join_date_XPATH).send_keys(join_date)

    def select_job_title_dropdown(self, job_title):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_job_title_dropdown_button_XPATH).click()
        job_title_dropdown_list = self.driver.find_elements(By.XPATH,
                                                            OrangeHrmElements.employee_job_title_dropdown_list_XPATH)
        for job_title_list in job_title_dropdown_list:
            if job_title == job_title_list.text:
                job_title_list.click()
                break

    def select_job_category_dropdown(self, job_category):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_job_category_dropdown_button_XPATH).click()
        job_category_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                               employee_job_category_dropdown_list_XPATH)
        for job_category_list in job_category_dropdown_list:
            if job_category == job_category_list.text:
                job_category_list.click()
                break

    def select_sub_unit_dropdown(self, sub_unit):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_sub_unit_dropdown_button_XPATH).click()
        sub_unit_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                           employee_sub_unit_dropdown_list_XPATH)
        for sub_unit_list in sub_unit_dropdown_list:
            if sub_unit == sub_unit_list.text:
                sub_unit_list.click()
                break

    def select_location_dropdown(self, location):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_location_dropdown_button_XPATH).click()
        location_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                           employee_location_dropdown_list_XPATH)
        for location_list in location_dropdown_list:
            if location == location_list.text:
                location_list.click()
                break

    def select_employment_status_dropdown(self, status):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employment_status_dropdown_button_XPATH).click()
        employment_status_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                                    employment_status_dropdown_list_XPATH)
        for employment_status_list in employment_status_dropdown_list:
            if status == employment_status_list.text:
                employment_status_list.click()
                break

    def click_employee_contract_toggle_button(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_contract_details_toggle_button_XPATH).click()

    def enter_employee_contract_start_end_date(self, start_date, end_date):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_contract_start_date_XPATH).send_keys(start_date)
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_contract_end_date_XPATH).send_keys(end_date)

    def click_employee_job_details(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_job_details_tap_XPATH).click()

    def click_employee_termination_and_activation_button(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.terminate_employment_and_activation_XPATH).click()

    def enter_employee_termination_date(self, date):

        self.driver.find_element(By.XPATH, OrangeHrmElements.termination_date_XPATH).send_keys(date)

    def select_employee_termination_reason_dropdown(self, reason):
        self.driver.find_element(By.XPATH, OrangeHrmElements.termination_reason_dropdown_button_XPATH).click()
        employee_termination_reason_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                                              termination_reason_dropdown_list_XPATH)
        for employee_termination_reason_list in employee_termination_reason_dropdown_list:
            if reason == employee_termination_reason_list.text:
                employee_termination_reason_list.click()
                break

    def click_employee_required_save(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.required_save_button).click()

    def click_employee_salary_component_tap(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_salary_tap_XPATH).click()

    def click_assigned_salary_component(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_salary_components_add_button_XPATH).click()

    def enter_employee_salary_component(self, component):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_salary_component_input_box_XPATH) \
            .send_keys(component)

    def select_pay_grade_dropdown(self, pay_grade):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_pay_grade_dropdown_button_XPATH).click()
        pay_grade_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                            employee_pay_grade_list_XPATH)
        for pay_grade_list in pay_grade_dropdown_list:
            if pay_grade == pay_grade_list.text:
                pay_grade_list.click()
                break

    def select_pay_frequency_dropdown(self, duration):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_pay_frequency_dropdown_button_XPATH).click()
        pay_frequency_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                                employee_pay_frequency_list_XPATH)
        for pay_frequency_list in pay_frequency_dropdown_list:
            if duration == pay_frequency_list.text:
                pay_frequency_list.click()
                break

    def select_currency_dropdown(self, currency):
        self.driver.find_element(By.XPATH, OrangeHrmElements.currency_dropdown_button_XPATH).click()
        currency_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                           currency_dropdown_button_XPATH)
        for currency_list in currency_dropdown_list:
            if currency == currency_list.text:
                currency_list.click()
                break

    def enter_employee_salary_amount(self, amount):
        self.driver.find_element(By.XPATH, OrangeHrmElements.salary_amount_input_box_XPATH).send_keys(amount)

    def click_direct_deposit_details_toggle_button(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.direct_deposit_details_toggle_button_XPATH).click()

    def enter_bank_account_number(self, ac_number):
        self.driver.find_element(By.XPATH, OrangeHrmElements.bank_account_number_input_box_XPATH).send_keys(ac_number)

    def select_bank_account_type_dropdown(self, ac_type):
        self.driver.find_element(By.XPATH, OrangeHrmElements.bank_account_type_dropdown_button_XPATH).click()
        bank_account_type_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                                    bank_account_type_list_XPATH)
        for bank_account_list in bank_account_type_dropdown_list:
            if ac_type == bank_account_list.text:
                bank_account_list.click()
                break

    def enter_bank_routing_number(self, route_number):
        self.driver.find_element(By.XPATH, OrangeHrmElements.bank_account_routing_number_input_box_XPATH) \
            .send_keys(route_number)

    def enter_deposit_amount(self, amount):
        self.driver.find_element(By.XPATH, OrangeHrmElements.deposit_amount_input_box_XPATH).send_keys(amount)

    def select_federal_income_tax_status_dropdown(self, status):
        self.driver.find_element(By.XPATH, OrangeHrmElements.federal_income_tax_status_dropdown_button_XPATH).click()
        federal_income_tax_status_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                                            federal_income_tax_status_list_XPATH)
        for federal_income_tax_status_list in federal_income_tax_status_dropdown_list:
            if status == federal_income_tax_status_list.text:
                federal_income_tax_status_list.click()
                break

    def select_state_income_tax_state_dropdown(self, state):
        self.driver.find_element(By.XPATH, OrangeHrmElements.state_income_tax_state_dropdown_button_XPATH).click()
        state_income_tax_status_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                                          state_income_tax_state_list_XPATH)
        for state_income_tax_state_list in state_income_tax_status_dropdown_list:
            if state == state_income_tax_state_list.text:
                state_income_tax_state_list.click()
                break

    def select_state_income_tax_status_dropdown(self, status):
        self.driver.find_element(By.XPATH, OrangeHrmElements.state_income_tax_status_dropdown_button_XPATH).click()
        state_income_tax_status_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                                          state_income_tax_status_list_XPATH)
        for state_income_tax_status_list in state_income_tax_status_dropdown_list:
            if status == state_income_tax_status_list.text:
                state_income_tax_status_list.click()
                break

    def select_state_income_tax_unemployment_state_dropdown(self, state):
        self.driver.find_element(By.XPATH, OrangeHrmElements.state_income_tax_unemployment_state_dropdown_button_XPATH) \
            .click()
        state_income_tax_unemployment_state_dropdown_list = self.driver. \
            find_elements(By.XPATH, OrangeHrmElements.state_income_tax_unemployment_state_list_XPATH)
        for state_income_tax_unemployment_state_list in state_income_tax_unemployment_state_dropdown_list:
            if state == state_income_tax_unemployment_state_list.text:
                state_income_tax_unemployment_state_list.click()
                break

    def select_state_income_tax_work_state_dropdown(self, state):
        self.driver.find_element(By.XPATH, OrangeHrmElements.state_income_tax_work_state_dropdown_button_XPATH).click()
        state_income_tax_work_state_dropdown_list = self.driver.find_elements(By.XPATH, OrangeHrmElements.
                                                                              state_income_tax_work_state_list_XPATH)
        for state_income_tax_work_state_list in state_income_tax_work_state_dropdown_list:
            if state == state_income_tax_work_state_list.text:
                state_income_tax_work_state_list.click()
                break

    def click_employee_stax_exemptions_tap(self):
        self.driver.find_element(By.XPATH, OrangeHrmElements.employee_tax_exemptions_tap_XPATH).click()