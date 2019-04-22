#!/usr/local/bin/python3
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from pages import *
from testCases import test_cases
from locators import *
from selenium.webdriver.common.by import By

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>


class TestPages(unittest.TestCase):

    def setUp(self):
        # HEADLESSブラウザに接続
        self.driver = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get("http://www.amazon.com")

    def test_page(self):
        # ページ表示
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

        # 検索
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        sPage = page.search_item("Nexus")

        # タブ選択
        print("\n" + str(test_cases(1)))
        # sPage = SearchPage(self.driver)
        sPage.push_side_pulldown()

        # ハイパーリンク選択
        print("\n" + str(test_cases(1)))
        sPage.push_a()


# def test_search_item(self):
#     print("\n" + str(test_cases(1)))
#     page = MainPage(self.driver)
#     search_result = page.search_item("Nexus")
# self.assertIn("Nexus", search_result)

# def test_sign_up_button(self):
#     print "\n" + str(test_cases(2))
#     page = MainPage(self.driver)
#     signUpPage = page.click_sign_up_button()
#     self.assertIn("ap/register", signUpPage.get_url())

# def test_sign_in_button(self):
#     print "\n" + str(test_cases(3))
#     page = MainPage(self.driver)
#     loginPage = page.click_sign_in_button()
#     self.assertIn("ap/signin", loginPage.get_url())

# def test_sign_in_with_valid_user(self):
#     print "\n" + str(test_cases(4))
#     mainPage = MainPage(self.driver)
#     loginPage = mainPage.click_sign_in_button()
#     result = loginPage.login_with_valid_user("valid_user")
#     self.assertIn("yourstore/home", result.get_url())

# def test_sign_in_with_in_valid_user(self):
#     print "\n" + str(test_cases(5))
#     mainPage = MainPage(self.driver)
#     loginPage = mainPage.click_sign_in_button()
#     result = loginPage.login_with_in_valid_user("invalid_user")
#     self.assertIn("There was a problem with your request", result)


def tearDown(self):
    print("end")
    self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
