import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_cart_button_exists(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    try:
        cartButton = browser.find_element(By.CSS_SELECTOR,"button.btn-add-to-basket")
        assert True
    except NoSuchElementException:
        assert False,"add to cart button not found"
    time.sleep(5)