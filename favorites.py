import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Testaddtofavorite:
    """Тесты добвления в избранное"""

    @pytest.fixture(scope="function")
    def driver(self):
        """Фикстура для инициализации драйвера"""
        driver = webdriver.Chrome()  # или webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()
    def test_succesful_add(self,driver):
        """Тест успешного добавления в избранное"""
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

        open_category_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/main/div[1]/div/div/div/div/div[1]/a")
        open_category_button.click()#Открываем категорию товара

        like_button_1 = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/main/section[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div[3]/div[2]/button[2]")
        like_button_1.click()#добавление товара 1 в избранное

        driver.execute_script("window.scrollBy(0, 500);")#скролл на 500 пикселей вниз

        like_button_2 = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/main/section[2]/div[2]/div/div[2]/div/div[3]/div[4]/div/div[3]/div[2]/button[2]")
        like_button_2.click()#добавление товара 2 в избранное

        driver.execute_script("window.scrollBy(0, -500);")  # скролл на 500 пикселей вверх

        favorite_screen_button = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/header/div/div[2]/div[5]/a[1]/span[2]")
        favorite_screen_button.click()#Открытие страницы "Избранное"

        driver.save_screenshot("screenshot.png") #Скриншот по окончанию теста


