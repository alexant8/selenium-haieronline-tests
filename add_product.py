import driver
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestAddproduct:
    """Тесты добавления в корзину"""

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

        catalog_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/header/div/div[2]/button[2]")
        catalog_button.click()#Открытие каталога

        climate_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/header/div/div[2]/div[4]/div/div/div/div/div[1]/ul/li[5]/a")
        climate_button.click()#Открытие раздела "Климатическия техника"

        driver.execute_script("window.scrollBy(0, 300);")  # скролл на 300 пикселей вниз

        add_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/main/div[1]/main/div/div[4]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/button[1]")
        add_button.click()#Добавить товар в корзину

        time.sleep(3)

        redirect_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/main/div[1]/main/div[2]/div/div/div[2]/div[3]/a/button")
        redirect_button.click()#Перейти в корзину

        delete_product_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div/div[2]/div[1]/section/div/div/div/div[1]/div[1]/div[2]/button/svg/path[2]")
        delete_product_button.click()#Удалить товар из корзины

