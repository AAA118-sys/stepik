from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(12)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    # first = browser.find_element(By.NAME, "firstname")
    # first.send_keys("Ivan")
    # second = browser.find_element(By.NAME, "lastname")
    # second.send_keys("Ivanov")
    # email = browser.find_element(By.NAME, "email")
    # email.send_keys("Ivanov@iv.vi")

    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'file.txt')
    # element = browser.find_element(By.ID, "file")
    # element.send_keys(file_path)

    # button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    # button.click()
    #
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    #
    input1 = browser.find_element(By.ID, "input_value")
    x = input1.text
    y = calc(x)

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()