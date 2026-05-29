import pytest
from selenium import webdriver

from HW_6.pages.login_page import LoginPage
from HW_6.pages.inventory_page import InventoryPage
from HW_6.pages.cart_page import CartPage
from HW_6.pages.checkout_page import CheckoutPage


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        options = webdriver.ChromeOptions()

        # Убрать всплывающее окно о смене пароля в гуглхром
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False
            }
        )

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

        self.driver.get("https://www.saucedemo.com/")

        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

        yield
        self.driver.quit()
