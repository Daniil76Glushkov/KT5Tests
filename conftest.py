import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def attach_screenshot(driver, description):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=description,
        attachment_type=allure.attachment_type.PNG,
    )


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
