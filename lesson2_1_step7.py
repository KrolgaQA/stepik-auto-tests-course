from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    # открываем страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение для x
    x = browser.find_element_by_tag_name("img").get_attribute("valuex")
    y = calc(x)
    
    # вводим значение в поле
    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)

    # Выбираем радиобаттон
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
    # Выбираем чекбокс
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    
    # жмакаем кнопку
    button = browser.find_element_by_css_selector("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()