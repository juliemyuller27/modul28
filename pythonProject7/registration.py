import pytest
from selenium.webdriver.common.by import By

from pages.locators import BasePageLocators
from pages.main_page import MainPage


@pytest.mark.positive
@pytest.mark.guest
@pytest.mark.parametrize("email", ["Julimyuller@yandex.ru", "Julimyuller1@yandex.ru", "Julimyuller2@yandex.ru", "Julimyuller3@yandex.ru"])
def test_register_from_main(browser, email):
    browser.implicitly_wait(5)
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.show_hover(*BasePageLocators.CABINET_BUTTON)
    page.choose_element(*BasePageLocators.CABINET_HOVER_REGISTER_BUTTON).click()
    browser.switch_to_active_element()
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите свой код скидки, телефон или эл.почту']").clear()
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите свой код скидки, телефон или эл.почту']").send_keys(email)

    assert browser.find_element(By.CSS_SELECTOR, "[data-default-value='Войти']").click()


@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.guest
@pytest.mark.parametrize("email", ["lolo, "", "l"*3065, "кккккк"*7777, "здзд"-66565, длдлдл, 4545, 484, 2,,5, 5.4, "   ", "|+*?:%;"№;%"])
def test_register_from_main_neg(browser, email):
    browser.implicitly_wait(5)
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.show_hover(*BasePageLocators.CABINET_BUTTON)
    page.choose_element(*BasePageLocators.CABINET_HOVER_REGISTER_BUTTON).click()
    browser.switch_to_active_element()
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите свой код скидки, телефон или эл.почту']").clear()
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите свой код скидки, телефон или эл.почту']").send_keys("email")

    assert browser.find_element(By.CSS_SELECTOR, "[data-default-value='Войти']").click()