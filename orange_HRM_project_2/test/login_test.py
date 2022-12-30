import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By

from orange_HRM_project_2.pages.orange_hrm_page_login import PageLogin
from orange_HRM_project_2.pages.orange_hrm_page_login import OrangeHrmElements


class LoginTestPage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_01_login_page_invalid_user_name(self):  # Test Case ID TC_Login_01
        driver = self.driver
        invalid_login = PageLogin(driver)
        invalid_login.user_login("admi1222", "admin123")
        alert_msg = driver.find_element(By.XPATH, OrangeHrmElements.invalid_credentials_XPATH).text
        assert alert_msg == "Invalid credentials"

    def test_02_login_page_invalid_password(self):  # Test Case ID TC_Login_02
        driver = self.driver
        invalid_login = PageLogin(driver)
        invalid_login.user_login("Admin", "12345")
        alert_msg = driver.find_element(By.XPATH, OrangeHrmElements.invalid_credentials_XPATH).text
        assert alert_msg == "Invalid credentials"

    def test_03_valid_login_page(self):  # Test Case ID TC_Login_03
        driver = self.driver
        valid_login = PageLogin(driver)
        valid_login.user_login("Admin", "admin123")
        dash_board = driver.find_element(By.XPATH, OrangeHrmElements.dashboard_text_XPATH).text
        assert dash_board == "Dashboard"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
