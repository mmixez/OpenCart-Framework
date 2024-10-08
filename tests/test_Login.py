import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import time

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("mmixez3@gmail.com")
        login_page.enter_password("yk123")
        login_page.click_on_login_button()
        account_page = AccountPage(self.driver)
        time.sleep(2)
        assert account_page.display_status_of_edit_your_account_information_option()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address(self.generate_email_with_random_string())
        login_page.enter_password("yk123")
        login_page.click_on_login_button()

        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("mmixez3@gmail.com")
        login_page.enter_password("yk12345")
        login_page.click_on_login_button()

        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("")
        login_page.enter_password("")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def generate_email_with_random_string(self):
        generatedString = ''.join(random.choices(string.ascii_letters, k=5))
        return generatedString + "@gmail.com"
