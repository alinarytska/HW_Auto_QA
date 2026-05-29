from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        first_name_input = self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_input = self.wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
        last_name_input.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        postal_code_input = self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
        postal_code_input.send_keys(postal_code)

    def click_continue(self):
        continue_button = self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        continue_button.click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def wait_for_overview_page(self):
        self.wait.until(EC.url_contains("checkout-step-two"))

    def get_total_price(self):
        total_label = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']")))
        return total_label.text
