import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Jian")
        register_page.enter_last_name("Kim")
        register_page.enter_email(self.generate_email_with_random_string())
        register_page.enter_telephone("1234567890")
        register_page.enter_password("12345")
        register_page.enter_password_confirm("12345")
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()

        expected_heading_text = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

        # assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # self.driver.find_element(By.LINK_TEXT, "Register").click()
        # self.driver.find_element(By.ID, "input-firstname").send_keys("Jian")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("Kim")
        # self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_with_random_string())
        # self.driver.find_element(By.ID,"input-telephone").send_keys("12345678")
        # self.driver.find_element(By.ID,"input-password").send_keys("12345")
        # self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        # self.driver.find_element(By.NAME, "agree").click()
        # self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()



    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Jian")
        register_page.enter_last_name("Kim")
        register_page.enter_email(self.generate_email_with_random_string())
        register_page.enter_telephone("1234567890")
        register_page.enter_password("12345")
        register_page.enter_password_confirm("12345")
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()
        time.sleep(2)
        expected_heading_text = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # self.driver.find_element(By.LINK_TEXT, "Register").click()
        # self.driver.find_element(By.ID, "input-firstname").send_keys("Jian")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("Kim")
        # self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_random_string())
        # self.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
        # self.driver.find_element(By.ID, "input-password").send_keys("12345")
        # self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        # self.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
        # self.driver.find_element(By.NAME, "agree").click()
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Jian")
        register_page.enter_last_name("Kim")
        register_page.enter_email("mmixez3@gmail.com")
        register_page.enter_telephone("1234567890")
        register_page.enter_password("12345")
        register_page.enter_password_confirm("12345")
        register_page.select_yes_radio_button()
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()

        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # self.driver.find_element(By.LINK_TEXT, "Register").click()
        # self.driver.find_element(By.ID, "input-firstname").send_keys("Jian")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("Kim")
        # self.driver.find_element(By.ID, "input-email").send_keys("mmmixez3@gmail.com")
        # self.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
        # self.driver.find_element(By.ID, "input-password").send_keys("12345")
        # self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        # self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
        # self.driver.find_element(By.NAME, "agree").click()
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_warning_text = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_dupliacte_email_warning().__contains__(expected_warning_text)



    def test_without_entering_any_field(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("")

        register_page.enter_last_name("")
        register_page.enter_email("")
        register_page.enter_telephone("")
        register_page.enter_password("")
        register_page.enter_password_confirm("")
        register_page.click_on_continue_button()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        # self.driver.find_element(By.LINK_TEXT, "Register").click()
        # self.driver.find_element(By.ID, "input-firstname").send_keys("")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("")
        # self.driver.find_element(By.ID, "input-email").send_keys("")
        # self.driver.find_element(By.ID, "input-telephone").send_keys("")
        # self.driver.find_element(By.ID, "input-password").send_keys("")
        # self.driver.find_element(By.ID, "input-confirm").send_keys("")
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_privacy_policy_warning_text = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_policy_warning().__eq__(expected_privacy_policy_warning_text)

        expected_first_name_warning_message = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieve_first_name_warning().__contains__(
            expected_first_name_warning_message)

        expected_last_name_warning_message = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieve_last_name_warning().__eq__(
            expected_last_name_warning_message)

        expected_email_warning_message = "E-Mail Address does not appear to be valid!"
        assert register_page.retrieve_email_warning().__eq__(
            expected_email_warning_message)

        expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
        assert register_page.retrieve_telephone_warning().__eq__(
            expected_telephone_warning_message)

        expected_password_warning_message = "Password must be between 4 and 20 characters!"
        assert register_page.retrieve_password_warning().__eq__(
            expected_password_warning_message)

    def generate_email_with_random_string(self):
        generatedString = ''.join(random.choices(string.ascii_letters, k=5))
        return generatedString + "@gmail.com"