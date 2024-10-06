from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name, "search_box_field_name", self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click("search_button_xpath", self.search_button_xpath)

    def click_on_my_account_drop_menu(self):
        self.element_click("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)

    def select_login_option(self):
        self.element_click("login_option_link_text", self.login_option_link_text)

    def naviage_to_login_page(self):
        return self.select_login_option()

    def select_register_option(self):
        self.element_click("register_option_link_text", self.register_option_link_text)
