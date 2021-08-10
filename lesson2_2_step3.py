from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def sum(x1, x2):
    return str(x1 + x2) # число в строку

try: 
    # открываем страницу
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение для x
    x1 = int(browser.find_element_by_id("num1").text) #строку в число
    x2 = int(browser.find_element_by_id("num2").text) #строку в число
    y = sum(x1, x2)
    # print (x1)
    # print (x2)
    # print (y)
    
    #вставляем значение в выпадашку
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)
    
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