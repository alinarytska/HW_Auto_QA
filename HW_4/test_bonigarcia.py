import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    yield driver
    driver.quit()


def test_third_image_alt_is_award(driver):
    wait = WebDriverWait(driver, 15)

    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    assert len(images) == 4

    third_image = driver.find_element(By.ID, "award")
    assert third_image.get_attribute("alt") == "award"
