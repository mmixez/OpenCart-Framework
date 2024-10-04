from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    search_box_field_name="search"

    def enter_product_into_search_box_field(self,product_name):
        self.driver.find_element(By.NAME,self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME,self.search_box_field_name).send_keys(product_name)



