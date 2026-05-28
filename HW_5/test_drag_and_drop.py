import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    yield driver
    driver.quit()


def accept_cookie_popup(driver, wait):
    cookie_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-cta-consent")))

    cookie_button.click()


def test_drag_and_drop_image_to_trash(driver):
    wait = WebDriverWait(driver, 10)
    accept_cookie_popup(driver, wait)

    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(iframe)

    gallery_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))
    first_photo = gallery_items[0]
    trash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))

    actions = ActionChains(driver)
    actions.drag_and_drop(first_photo, trash).perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    trash_items = driver.find_elements(By.CSS_SELECTOR, "#trash li")
    gallery_items = driver.find_elements(By.CSS_SELECTOR, "#gallery li")

    assert len(trash_items) == 1
    assert len(gallery_items) == 3
