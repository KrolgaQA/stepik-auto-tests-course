from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

try:

    # считываем значение для x и считаем функцию
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # вводим значение в поле
    input_element = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_element)
    input_element.send_keys(y)
    
    # Выбираем радиобаттон
    option1 = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    
    # Выбираем чекбокс
    option1 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    
    # чтобы кликнуть по кнопке, перекрытой футером
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
    button.click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()