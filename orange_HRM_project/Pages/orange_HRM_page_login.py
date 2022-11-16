
from selenium import webdriver
from selenium.webdriver.common.by import By

from orange_HRM_project.Pages.orange_HRM_web_elements import Orange_HRM_Elements


class Page_Login:

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.user_name_text_box_XPATH).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.password_text_box_XPATH).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, Orange_HRM_Elements.login_button_XPATH).click()





