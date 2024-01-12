from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.maximize_window()
time.sleep(2)


def text_area(xpath, text):
    input = driver.find_element(By.NAME, xpath)
    input.send_keys(text)


def dropdown(xpath, index):
    arrow = driver.find_element(By.NAME, xpath)
    drop = Select(arrow)
    drop.select_by_index(index)


def radio(xpath):
    radio = driver.find_element(By.ID, xpath)
    radio.click()


text_area("my-text", "Willian Giovanini Dei Tosi")
time.sleep(1)
text_area("my-password", "1111122222")
time.sleep(1)
text_area("my-textarea", "usando Selenium para automatizar este formulario")
time.sleep(1)
dropdown("my-select", 1)
time.sleep(1)
text_area("my-datalist", "São Paulo")
time.sleep(1)
radio("my-check-2")
time.sleep(1)
radio("my-check-1")
time.sleep(1)
radio("my-radio-2")
time.sleep(1)

submit = driver.find_element(By.XPATH, f"//button[contains(text(), 'Submit')]").click()
time.sleep(3)

driver.quit()
