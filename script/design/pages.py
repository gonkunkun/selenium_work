#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators import *
from selenium.webdriver.support.ui import WebDriverWait


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage():
    def __init__(self, driver):
        self.driver = driver
        self.locator = MainPageLocatars
        # super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.driver.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.driver.find_element(*self.locator.SEARCH).send_keys(item)
        self.driver.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        return SearchPage(self.driver)
        # return self.driver.find_element(*self.locator.SEARCH_LIST).text

#     def click_sign_up_button(self):
#         self.hover(*self.locator.ACCOUNT)
#         self.find_element(*self.locator.SIGNUP).click()
#         return SignUpPage(self.driver)

#     def click_sign_in_button(self):
#         self.hover(*self.locator.ACCOUNT)
#         self.find_element(*self.locator.LOGIN).click()
#         return LoginPage(self.driver)


class SearchPage():
    def __init__(self, driver):
        self.driver = driver
        self.locator = SearchPageLocators

    def push_side_pulldown(self):
        self.driver.find_element(*self.locator.SEE_MORE).click()

    def push_a(self):
        self.driver.find_element(*self.locator.A).click()


# class LoginPage(Page):
#     def __init__(self, driver):
#         self.locator = LoginPageLocatars
#         super(LoginPage, self).__init__(driver)  # Python2 version

#     def enter_email(self, user):
#         self.find_element(
#             *self.locator.EMAIL).send_keys(users.get_user(user)["email"])

#     def enter_password(self, user):
#         self.find_element(
#             *self.locator.PASSWORD).send_keys(users.get_user(user)["password"])

#     def click_login_button(self):
#         self.find_element(*self.locator.SUBMIT).click()

#     def login(self, user):
#         self.enter_email(user)
#         self.enter_password(user)
#         self.click_login_button()

#     def login_with_valid_user(self, user):
#         self.login(user)
#         return HomePage(self.driver)

#     def login_with_in_valid_user(self, user):
#         self.login(user)
#         return self.find_element(*self.locator.ERROR_MESSAGE).text


# class HomePage(Page):
#     pass


# class SignUpPage(Page):
#     pass
