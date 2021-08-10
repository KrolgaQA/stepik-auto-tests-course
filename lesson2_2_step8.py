from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    # заполняем обязательные поля
    elements = browser.find_elements_by_xpath("//input[@type = 'text'][@required]")
    for element in elements:
        element.send_keys("Мой ответ")
        
    #отправляем файл
    file_send = browser.find_element_by_id("file")
    file_send.send_keys(file_path)
    
    # чтобы кликнуть по кнопке, перекрытой футером
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) 
    button.click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()