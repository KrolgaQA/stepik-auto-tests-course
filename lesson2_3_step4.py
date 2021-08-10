from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    # открываем страницу
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # жмакаем кнопку
    button = browser.find_element_by_css_selector("button")
    button.click()
    
    # переключаемся на алерт и соглашаемся
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # считываем значение для x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # вводим значение в поле
    input_element = browser.find_element_by_css_selector("#answer")
    input_element.send_keys(y)

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