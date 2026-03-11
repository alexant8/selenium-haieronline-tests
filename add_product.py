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

            # Возврат в корзину
            back_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[5]/div[1]/main/div[1]/main/div[1]/div[1]/div/section/button")
            ))
            back_button.click()
            print("✓ Возврат в корзину")
            time.sleep(2)

            # Удаление товара
            delete_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/div[5]/div[1]/main/div[1]/main/div/div[2]/div[1]/section/div/div/div/div[1]/div[1]/div[2]/button")
            ))
            delete_button.click()
            print("✓ Удаление товара")
            time.sleep(2)

            # Кнопка "Оставить товар" (отмена удаления)
            try:
                keep_button = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[5]/div[1]/div[1]/div/div/div/div[2]/div/div[3]/button[1]")
                ))
                keep_button.click()
                print("✓ Кнопка 'Оставить товар' нажата")
                time.sleep(2)
            except:
                print("⚠ Кнопка 'Оставить товар' не найдена")

            # Удаление товара
            delete_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH,
                    "/html/body/div[5]/div[1]/main/div[1]/main/div/div[2]/div[1]/section/div/div/div/div[1]/div[1]/div[2]/button")
            ))
            delete_button.click()
            print("✓ Удаление товара")
            time.sleep(2)

            # Подтверждение удаления
            try:
                confirm_delete = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#js-teleport-container > div > div > div > div.modal-body > div > div.h-reset-modal__buttons > button.h-button.h-button--main.h-button--h56.h-button--fw500.h-button--rounding-m")
                ))
                confirm_delete.click()
                print("✓ Удаление подтверждено")
                time.sleep(2)
            except:
                print("⚠ Кнопка подтверждения удаления не найдена")

            print("\n" + "=" * 50)
            print("✓ ТЕСТ РАБОТЫ С КОРЗИНОЙ УСПЕШНО ЗАВЕРШЕН!")
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