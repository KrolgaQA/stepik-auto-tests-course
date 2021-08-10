from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    # открываем страницу
    link = " http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение для x
    x_element = browser.find_element_by_css_selector(".form-group > label :nth-child(2)")
    x = x_element.text
    y = calc(x)
    
    # вводим значение в поле
    input_element = browser.find_element_by_css_selector("#answer")
    input_element.send_keys(y)

    # Выбираем радиобаттон
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    
    # Выбираем чекбокс
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
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