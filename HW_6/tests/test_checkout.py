from HW_6.tests.base_test import BaseTest


class TestCheckout(BaseTest):
    def test_add_items_to_cart(self):
        self.login_page.login("standard_user", "secret_sauce")

        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.add_bolt_t_shirt_to_cart()
        self.inventory_page.add_onesie_to_cart()

        self.inventory_page.go_to_cart()
        assert "cart" in self.driver.current_url

        self.cart_page.click_checkout()
        assert "checkout-step-one" in self.driver.current_url

        self.checkout_page.fill_checkout_form("Tom", "Hart", "01067")

        self.checkout_page.wait_for_overview_page()

        total_price = self.checkout_page.get_total_price()
        assert total_price == "Total: $58.29"
