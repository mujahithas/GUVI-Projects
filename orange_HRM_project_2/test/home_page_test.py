import unittest
from selenium import webdriver

from orange_HRM_project_2.pages.orange_home_page import HomePage
from orange_HRM_project_2.pages.orange_hrm_page_login import PageLogin


class HomeTestPage(unittest.TestCase):
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

    def test_01_validate_home_search_text_box(self):  # Test Case ID TC_PIM_01
        driver = self.driver
        search_text_lower = ["admin", "pim", "leave", "time", "recruitment", "my info", "performance", "dashboard",
                             "directory", "maintenance", "buzz"]
        search_text_upper = ["ADMIN", "PIM", "LEAVE", "TIME", "RECRUITMENT", "MY INFO", "PERFORMANCE", "DASHBOARD",
                             "DIRECTORY", "MAINTENANCE", "BUZZ"]
        home_search_text_box = HomePage(driver)
        home_search_text_box.validate_home_page_search_text_box(search_text_lower)
        home_search_text_box.validate_home_page_search_text_box(search_text_upper)
        assert home_search_text_box.result_data.sort() == home_search_text_box.home_page_list.sort()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
