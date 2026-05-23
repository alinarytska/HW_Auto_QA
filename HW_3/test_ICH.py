import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    sleep(3)

    yield driver
    driver.quit()


def test_logo_is_displayed(driver):
    logo = driver.find_element(By.CSS_SELECTOR, "[alt='IT Career Hub']")
    assert logo.is_displayed()


def test_programs_link_is_displayed(driver):
    programs_link = driver.find_element(By.LINK_TEXT, "Программы")
    assert programs_link.is_displayed()


def test_payment_methods_link_is_displayed(driver):
    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    assert payment_link.is_displayed()


def test_about_link_is_displayed(driver):
    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    assert about_link.is_displayed()


# Вспомогательная функция, открывающая меню 'О нас'
def open_about_menu(driver):
    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    about_link.click()
    sleep(2)


def test_contacts_link_is_displayed(driver):
    open_about_menu(driver)
    contacts_link = driver.find_element(By.LINK_TEXT, "Контакты")
    assert contacts_link.is_displayed()


def test_reviews_link_is_displayed(driver):
    reviews_link = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert reviews_link.is_displayed()


def test_blog_link_is_displayed(driver):
    blog_link = driver.find_element(By.LINK_TEXT, "Блог")
    assert blog_link.is_displayed()


def test_language_switching(driver):
    # Проверка отображения кнопок
    ru_button = driver.find_element(By.LINK_TEXT, "ru")
    de_button = driver.find_element(By.LINK_TEXT, "de")

    assert ru_button.is_displayed()
    assert de_button.is_displayed()

    # Переключение на немецкий
    de_button.click()
    sleep(3)

    assert driver.current_url == "https://itcareerhub.de/"
    assert "Erwerben Sie einen gefragten IT-Beruf" in driver.page_source

    # Переключение обратно на русский
    ru_button = driver.find_element(By.LINK_TEXT, "ru")

    ru_button.click()
    sleep(3)

    assert driver.current_url == "https://itcareerhub.de/ru"
    assert "Освойте актуальные цифровые профессии" in driver.page_source


def test_callback_popup_text_is_displayed(driver):
    open_about_menu(driver)

    contacts_link = driver.find_element(By.LINK_TEXT, "Контакты")
    contacts_link.click()
    sleep(3)

    callback_button = driver.find_element(By.LINK_TEXT, "ОБРАТНЫЙ ЗВОНОК")

    # Принудительный клик
    driver.execute_script("arguments[0].click();", callback_button)
    sleep(3)

    popup_text = driver.find_element(By.CSS_SELECTOR,"[field='tn_text_175871291756015470']")

    assert popup_text.is_displayed()
    assert "Запишитесь на бесплатную карьерную консультацию" in popup_text.text
