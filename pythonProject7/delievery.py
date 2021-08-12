import datetime

from pages.main_page import MainPage

def test_delivery_valid_date(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    delivery_date = page.get_delivery_date(browser)
    now = datetime.datetime.now()

    assert (delivery_date - now).days < 4