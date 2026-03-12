import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestAddproduct:
    """Тесты добавления в корзину"""

    @pytest.fixture(scope="function")
    def driver(self):
        """Фикстура для инициализации драйвера"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_successful_login(self, driver):
        """Тест успешной авторизации"""
        wait = WebDriverWait(driver, 15)

        try:
            print("\n" + "=" * 50)
            print("ТЕСТ: Успешная авторизация")
            print("=" * 50)

            # Переход на страницу
            driver.get("https://haieronline.ru/")
            print("✓ Страница загружена")

            # Ждем загрузку body
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            time.sleep(2)

            # Кнопка "Войти"
            enter_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[26]/div[1]/header/div/div[2]/div[5]/a[3]/div")
            ))
            enter_button.click()
            print("✓ Кнопка 'Войти' нажата")
            time.sleep(2)

            # Кнопка "Войти по паролю"
            password_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[3]/button[2]")
            ))
            password_button.click()
            print("✓ Кнопка 'Войти по паролю' нажата")
            time.sleep(2)

            # Поле email
            email_input = wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[1]/input")
            ))
            email_input.click()
            email_input.clear()
            email_input.send_keys("alexant3003@gmail.com")
            print("✓ Email введен")
            time.sleep(1)

            # Поле пароля
            password_input = wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[2]/div[2]/input")
            ))
            password_input.click()
            password_input.clear()
            password_input.send_keys("123456")
            print("✓ Пароль введен")
            time.sleep(1)

            # Кнопка авторизации
            auth_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[26]/div[2]/div/div/div/div[2]/form/div[4]")
            ))
            auth_button.click()
            print("✓ Кнопка авторизации нажата")
            time.sleep(3)

            print("✓ ТЕСТ АВТОРИЗАЦИИ УСПЕШНО ЗАВЕРШЕН!")

        except TimeoutException:
            print("❌ Ошибка: Элемент не найден за 15 секунд")
            assert False, "Таймаут при ожидании элемента"
        except NoSuchElementException as e:
            print(f"❌ Ошибка: Элемент не найден - {e}")
            assert False, f"Элемент не найден: {e}"
        except Exception as e:
            print(f"❌ Непредвиденная ошибка: {e}")
            assert False, f"Ошибка: {e}"

    def test_full_cart_flow(self, driver):
        """Полный тест работы с корзиной (после авторизации)"""
        # Сначала выполняем авторизацию
        self.test_successful_login(driver)

        wait = WebDriverWait(driver, 15)

        try:
            print("\n" + "=" * 50)
            print("ТЕСТ: Работа с корзиной")
            print("=" * 50)

            # Открытие каталога
            catalog_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[6]/div[1]/header/div/div[2]/button[2]")
            ))
            catalog_button.click()
            print("✓ Каталог открыт")
            time.sleep(2)

            # Раздел "Климатическая техника"
            climate_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[6]/div[1]/header/div/div[2]/div[4]/div/div/div/div/div[1]/ul/li[5]/a")
            ))
            climate_button.click()
            print("✓ Раздел климатической техники открыт")
            time.sleep(3)

            # Ожидание загрузки товаров
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'product')]")
            ))

            # Скролл
            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(2)

            # Добавление товара
            add_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/div[6]/div[1]/main/div[1]/main/div/div[4]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/button[1]")
            ))
            add_button.click()
            print("✓ Товар добавлен в корзину")
            time.sleep(3)

            # Переход в корзину
            cart_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[6]/div[1]/main/div[1]/main/div[2]/div/div/div[2]/div[3]/a/button")
            ))
            cart_button.click()
            print("✓ Переход в корзину")
            time.sleep(3)

            # Оформление заказа
            order_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div/div[2]/div[2]/aside/div/div[3]/button")
            ))
            order_button.click()
            print("✓ Оформление заказа")
            time.sleep(3)

            # Раскрыть список городов
            list_city_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div[1]/div[2]/div[1]/section[2]/div[3]/form/div[1]/div[1]/div/div/button")
            ))
            list_city_button.click()
            print("✓ Список городов раскрыт")


            # Выбрать город
            city_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div[1]/div[2]/div[1]/section[2]/div[3]/form/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/input")
            ))
            city_input.click()
            city_input.clear()
            city_input.send_keys("Рязань")
            print("✓ Город выбран")

            #Выбрать улицу
            Street_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div[1]/div[2]/div[1]/section[2]/div[3]/form/div[1]/div[2]/div/div/div/div[1]/input")
            ))
            Street_input.click()
            Street_input.clear()
            Street_input.send_keys("ул Пирогова")
            print("✓ Улица выбрана")

            # Выбрать дом
            House_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/div[5]/div[1]/main/div[1]/main/div[1]/div[2]/div[1]/section[2]/div[3]/form/div[1]/div[3]/div/div/div/div[1]/input")
            ))
            House_input.click()
            House_input.clear()
            House_input.send_keys("55")
            print("✓ Дом выбран")

            # Выбрать квартиру
            flat_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div[1]/div[2]/div[1]/section[2]/div[3]/form/div[1]/div[3]/div/div/div/div[1]/input")
            ))
            flat_input.click()
            flat_input.clear()
            flat_input.send_keys("5")
            print("✓ Квартира выбрана")

            # Выбрать подъезд
            entrance_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div[1]/div[2]/div[1]/section[2]/div[3]/form/div[1]/div[5]/div/div[1]/input")
            ))
            entrance_input.click()
            entrance_input.clear()
            entrance_input.send_keys("3")
            print("✓ Подъезд выбран")

            # Выбрать Этаж
            flor_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div[1]/div[2]/div[1]/section[2]/div[3]/form/div[1]/div[6]/div/div[1]/input")
            ))
            flor_input.click()
            flor_input.clear()
            flor_input.send_keys("1")
            print("✓ Этаж выбран")

            # Написать код от домофона
            Code_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div[1]/div[2]/div[1]/section[2]/div[3]/form/div[1]/div[7]/div/div[1]/input")
            ))
            Code_input.click()
            Code_input.clear()
            Code_input.send_keys("123456")
            print("✓ Код написан")

            # Коментарий к заказу

            print("\n" + "=" * 50)
            print("✓ ТЕСТ РАБОТЫ ЗАПОЛНЕНИЯ ДАННЫХ ЗАВЕРШЕН!")
            print("=" * 50)

        except TimeoutException:
            print("❌ Ошибка: Элемент не найден за 15 секунд")
            assert False, "Таймаут при ожидании элемента"
        except NoSuchElementException as e:
            print(f"❌ Ошибка: Элемент не найден - {e}")
            assert False, f"Элемент не найден: {e}"
        except Exception as e:
            print(f"❌ Непредвиденная ошибка: {e}")
            assert False, f"Ошибка: {e}"


if __name__ == "__main__":
    # Запуск тестов
    pytest.main([__file__, "-v", "-s"])