from selenium.webdriver.common.by import By
import time

def test_button_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_cart = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button_cart != None, "Add to cart button not found"