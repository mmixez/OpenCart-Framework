from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath="//div[@id='account-login']/div[1]"

    def enter_email_address(self,email_address_text):
        self.type_into_element(email_address_text,"email_address_field_id", self.email_address_field_id)
        # self.driver.find_element(By.ID, self.email_address_field_id).click()
        # self.driver.find_element(By.ID, self.email_address_field_id).clear()
        # self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address_text)

    def enter_password(self,password_text):
        self.type_into_element(password_text,"password_field_id", self.password_field_id)
        # self.driver.find_element(By.ID, self.password_field_id).click()
        # self.driver.find_element(By.ID, self.password_field_id).clear()
        # self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def click_on_login_button(self):
        self.element_click("login_button_xpath", self.login_button_xpath)
        #self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def retrieve_warning_message(self):
        return self.retrieve_element_text("warning_message_xpath",self.warning_message_xpath)
        #  return self.driver.find_element(By.XPATH,self.warning_message_xpath).text


