import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    yield driver
    driver.quit()


def test_iframe_text_is_displayed(driver):
    wait = WebDriverWait(driver, 10)

    iframe = wait.until(EC.presence_of_element_located((By.ID, "my-iframe")))

    driver.switch_to.frame(iframe)

    paragraphs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lead")))

    expected_text = "semper posuere integer et senectus justo curabitur."

    found = False

    for paragraph in paragraphs:
        if expected_text in paragraph.text:
            found = True

    assert found
