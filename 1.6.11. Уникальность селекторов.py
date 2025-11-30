from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

try:
    # Для тестирования на registration1.html раскомментируйте строку ниже
    link = "http://suninjuly.github.io/registration1.html"

    # Для тестирования на registration2.html раскомментируйте строку ниже
    #link = "http://suninjuly.github.io/registration2.html"

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)

    browser.get(link)

    # Заполняем обязательные поля с использованием уникальных селекторов
    first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    first_name.send_keys("Konstantin")

    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    email.send_keys("KPetrov@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
    print("Тест пройден успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    time.sleep(10)
    browser.quit()