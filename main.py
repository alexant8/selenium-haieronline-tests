import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestAuthorization:
    """Тесты авторизации"""

    @pytest.fixture(scope="function")
    def driver(self):
        """Фикстура для инициализации драйвера"""
        driver = webdriver.Chrome()  # или webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_successful_login(self, driver):
        """Тест успешной авторизации"""
        # Переход на страницу авторизации
        driver.get("https://haieronline.ru/")

        enter_button = driver.find_element(By.XPATH, "/html/body/div[26]/div[1]/header/div/div[2]/div[5]/a[3]/div")
        enter_button.click() #Открыли форму авторизации

        password_button = driver.find_element(By.XPATH,"/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[3]/button[2]")
        password_button.click()#Открыли форму автоиизации по паролю

        email_string_button = driver.find_element(By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[1]")
        email_string_button.click()#Установка курсора в поле ввода

        email_selectors = driver.find_element(By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[1]/input")
        email_selectors.send_keys("alexant3003@gmail.com")#Ввод почты

        password_string_button = driver.find_element(By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[2]")
        password_string_button.click()#Установка курсора в поле ввода

        password_selectors = driver.find_element(By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[2]/input")
        password_selectors.send_keys("123456")#Ввод пароля

        auth_button = driver.find_element(By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[4]")
        auth_button.click()#Клик по кнопке авторизации

        driver.save_screenshot("success_auth.png")#Сделать скриншот
    def test_invalid_credentials(self, driver):
         """Тест с неверными учетными данными"""
         # Переход на страницу авторизации
         driver.get("https://haieronline.ru/")

         enter_button = driver.find_element(By.XPATH, "/html/body/div[26]/div[1]/header/div/div[2]/div[5]/a[3]/div")
         enter_button.click()  # Открыли форму авторизации

         password_button = driver.find_element(By.XPATH,"/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[3]/button[2]")
         password_button.click()  # Открыли форму автоиизации по паролю

         email_string_button = driver.find_element(By.XPATH,"/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[1]")
         email_string_button.click()  # Установка курсора в поле ввода

         email_selectors = driver.find_element(By.XPATH,"/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[1]/input")
         email_selectors.send_keys("alexant1996@yandex.ru")  # Ввод почты

         password_string_button = driver.find_element(By.XPATH,"/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[2]")
         password_string_button.click()  # Установка курсора в поле ввода

         password_selectors = driver.find_element(By.XPATH,"/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[2]/input")
         password_selectors.send_keys("123456")  # Ввод пароля

         auth_button = driver.find_element(By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[4]")
         auth_button.click()  # Клик по кнопке авторизации

    def test_empty_fields(self, driver):
        """Тест с пустыми полями"""
        # Переход на страницу авторизации
        driver.get("https://haieronline.ru/")

        enter_button = driver.find_element(By.XPATH, "/html/body/div[26]/div[1]/header/div/div[2]/div[5]/a[3]/div")
        enter_button.click()  # Открыли форму авторизации

        password_button = driver.find_element(By.XPATH,
                                              "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[3]/button[2]")
        password_button.click()  # Открыли форму автоиизации по паролю

        auth_button = driver.find_element(By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[4]")
        auth_button.click()  # Клик по кнопке авторизации
