import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import time


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_login_with_valid_credentials(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("mmixez3@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("yk123")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()

    def test_login_with_invalid_email_and_valid_password(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_random_string())
        self.driver.find_element(By.ID, "input-password").send_keys("yk123")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class ='alert alert-danger alert-dismissible']").text.__contains__(expected_warning_message)

    # def test_login_with_valid_email_and_invalid_password(self):
    #
    #     self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    #     self.driver.find_element(By.LINK_TEXT, "Login").click()
    #     self.driver.find_element(By.ID, "input-email").send_keys("mmmixez3@gmail.com")
    #     self.driver.find_element(By.ID, "input-password").send_keys("yk12345")
    #     self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
    #     expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    #     assert self.driver.find_element(By.XPATH, "//div[@class ='alert alert-danger alert-dismissible']").text.__contains__(
    #         expected_warning_message)

    def test_login_with_invalid_email_and_invalid_password(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_random_string())
        self.driver.find_element(By.ID, "input-password").send_keys("yk12345")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class ='alert alert-danger alert-dismissible']").text.__contains__(
            expected_warning_message)

    def test_login_without_entering_credentials(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class ='alert alert-danger alert-dismissible']").text.__contains__(
            expected_warning_message)

    def generate_email_with_random_string(self):
        generatedString = ''.join(random.choices(string.ascii_letters, k=5))
        return generatedString + "@gmail.com"




#validEmail= mmixez3@gmail.com
#validPassword = yk123