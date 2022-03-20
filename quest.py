import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


try:
    link = " http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    button.click()

    browser.execute_script("window.scrollBy(0, 300);")

    num = browser.find_element_by_id("input_value").text

    inputnum = browser.find_element_by_id("answer")
    inputnum.send_keys(str(math.log(abs(12*math.sin(int(num))))))

    button = browser.find_element_by_id("solve")
    button.click()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
finally:
    time.sleep(20)
    browser.quit()