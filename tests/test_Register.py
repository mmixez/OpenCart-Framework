import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string



@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_register_with_mandatory_fields(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Jian")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Kim")
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_with_random_string())
        self.driver.find_element(By.ID,"input-telephone").send_keys("12345678")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_heading_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)


    def test_register_with_all_fields(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Jian")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Kim")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_random_string())
        self.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_heading_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)


    def test_register_with_duplicate_email(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Jian")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Kim")
        self.driver.find_element(By.ID, "input-email").send_keys("mmmixez3@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys("12345678")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_warning_text = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expected_warning_text)



    def test_without_entering_any_field(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("")
        self.driver.find_element(By.ID, "input-lastname").send_keys("")
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-telephone").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.ID, "input-confirm").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_privacy_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expected_privacy_policy_warning_message)

        expected_first_name_warning_message = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div").text.__eq__(expected_first_name_warning_message)

        expected_last_name_warning_message = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(
            expected_last_name_warning_message)


        expected_email_warning_message = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(
            expected_email_warning_message)

        expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(
            expected_telephone_warning_message)

        expected_password_warning_message = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(
            expected_password_warning_message)

    def generate_email_with_random_string(self):
        generatedString = ''.join(random.choices(string.ascii_letters, k=5))
        return generatedString + "@gmail.com"