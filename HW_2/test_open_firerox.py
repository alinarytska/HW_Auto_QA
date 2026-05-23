import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_payment_methods_section(driver):
    driver.get("https://itcareerhub.de/ru/")
    sleep(5)

    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()
    sleep(5)

    payment_section = driver.find_element(By.CSS_SELECTOR, "#rec1921734713 > div > div > div.t396__filter")
    payment_section.screenshot("./payment_methods_section.png")

