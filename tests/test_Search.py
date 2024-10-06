import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_valid_product()


        # self.driver.find_element(By.NAME,"search").send_keys("HP")
        #self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        #assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("Honda")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_text)
        # self.driver.find_element(By.NAME, "search").send_keys("Honda")
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        # assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("")
        home_page.click_on_search_button()
        expected_text = "There is no product that matches the search criteria."
        # self.driver.find_element(By.NAME, "search").send_keys("")
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        search_page = SearchPage(self.driver)
        assert search_page.retrieve_no_product_message().__eq__(expected_text)




# driver = webdriver.Chrome()
#
# driver.get("https://tutorialsninja.com/demo/")
# search_button = driver.find_element(By.XPATH, "//div[@id='search']//button")
#
# search_button.screenshot("12")
#
# driver.quit()