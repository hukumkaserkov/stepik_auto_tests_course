import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Enter first name')]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Enter last name')]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Enter email')]")
    input3.send_keys("test@test.ru")

    # Вставляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Stepik.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
