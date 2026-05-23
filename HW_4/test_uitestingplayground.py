import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("http://uitestingplayground.com/textinput")

    yield driver
    driver.quit()


def test_button_text_changed(driver):
    wait = WebDriverWait(driver, 10)

    input_field = wait.until(EC.visibility_of_element_located((By.ID, "newButtonName")))
    input_field.send_keys("ITCH")

    button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
    button.click()

    wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH"))

    assert button.text == "ITCH"

