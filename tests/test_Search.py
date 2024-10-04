import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_search_for_a_valid_product(self):

        self.driver.find_element(By.NAME,"search").send_keys("HP")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    def test_search_for_an_invalid_product(self):

        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

    def test_search_without_entering_any_product(self):

        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)




# driver = webdriver.Chrome()
#
# driver.get("https://tutorialsninja.com/demo/")
# search_button = driver.find_element(By.XPATH, "//div[@id='search']//button")
#
# search_button.screenshot("12")
#
# driver.quit()