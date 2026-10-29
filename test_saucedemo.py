import allure
from selenium.webdriver.common.by import By

from conftest import attach_screenshot


USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def login(driver):
    with allure.step("Ввести логин"):
        driver.find_element(By.ID, "user-name").send_keys(USERNAME)

    with allure.step("Ввести пароль"):
        driver.find_element(By.ID, "password").send_keys(PASSWORD)

    with allure.step("Нажать кнопку Login"):
        driver.find_element(By.ID, "login-button").click()


@allure.title("Успешный вход в магазин")
def test_login(driver):
    """Проверка входа зарегистрированного пользователя."""
    with allure.step("Открыть страницу авторизации"):
        assert "Swag Labs" in driver.title

    login(driver)

    with allure.step("Проверить, что открылась страница товаров"):
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    attach_screenshot(driver, "Успешный вход в магазин")


@allure.title("Добавление товара в корзину")
def test_add_product_to_cart(driver):
    """Проверка добавления товара в корзину."""
    login(driver)

    with allure.step("Добавить рюкзак в корзину"):
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    with allure.step("Открыть корзину"):
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    with allure.step("Проверить товар в корзине"):
        product = driver.find_element(
            By.CSS_SELECTOR, ".cart_item .inventory_item_name"
        )
        assert product.text == "Sauce Labs Backpack"

    attach_screenshot(driver, "Товар добавлен в корзину")


@allure.title("Оформление заказа с заполнением формы")
def test_checkout_form(driver):
    """Проверка формы покупателя и завершения заказа."""
    login(driver)

    with allure.step("Добавить товар и перейти в корзину"):
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    with allure.step("Открыть форму оформления заказа"):
        driver.find_element(By.ID, "checkout").click()

    with allure.step("Заполнить имя, фамилию и почтовый индекс"):
        driver.find_element(By.ID, "first-name").send_keys("Ivan")
        driver.find_element(By.ID, "last-name").send_keys("Ivanov")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

    with allure.step("Продолжить и проверить товар в заказе"):
        driver.find_element(By.ID, "continue").click()
        assert driver.find_element(By.CLASS_NAME, "title").text == "Checkout: Overview"
        assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"

    with allure.step("Завершить заказ и проверить сообщение об успехе"):
        driver.find_element(By.ID, "finish").click()
        assert driver.find_element(By.CLASS_NAME, "complete-header").text == "Thank you for your order!"

    attach_screenshot(driver, "Заказ успешно оформлен")
