import unittest
from selenium import webdriver
from orange_HRM_project_2.pages.orange_admin_module import AdminPage
from orange_HRM_project_2.pages.orange_hrm_page_login import PageLogin


class AdminTestPage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver = cls.driver
        invalid_login = PageLogin(driver)
        invalid_login.user_login("Admin", "admin123")

    def test_01_validate_admin_user_management(self):  # Test Case ID TC_PIM_02
        driver = self.driver
        user_role_list_data = ["-- Select --", "Admin", "ESS"]
        statu_list_data = ["-- Select --", "Enabled", "Disabled"]
        user_management = AdminPage(driver)
        user_management.click_admin()
        user_management.click_user_management()
        user_management.click_user_role_dropdown()
        assert user_role_list_data == user_management.role_dropdown_expect_result
        user_management.click_user_status_dropdown()
        assert statu_list_data == user_management.status_dropdown_expect_result

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
