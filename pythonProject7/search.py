import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage


@pytest.mark.parametrize("search_string", ["lolo, "", "l"*3065, "кккккк"*7777, "здзд"-66565, длдлдл, 4545, 484, 2,,5, 5.4, "   ", "|+*?:%;"№;%"])
def test_guest_can_see_search_results(browser, search_string):
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.search(search_string)

    result_page = BasePage(browser, page.browser.current_url)
    result_text = result_page.choose_element(By.CSS_SELECTOR, "h1").text

@pytest.mark.parametrize("search_string", ["Пушкин"])

    def test_guest_can_see_search_results(browser, search_string):
        page = MainPage(browser, MainPage.URL)
        page.open_page()
        page.search(search_string)

    expected_text1 = "Все, что мы нашли в Лабиринте по запросу «Пушкин»"
    expected_text2 = "Мы ничего не нашли по вашему запросу! Что делать?"

    assert result_text == expected_text1 or result_text == expected_text2
