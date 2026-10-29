# Selenium + Pytest + Allure

Сайт: https://www.saucedemo.com/

Три теста:
1. Успешный вход в магазин.
2. Добавление рюкзака в корзину и проверка его названия.
3. Заполнение формы покупателя и завершение заказа.

В тестах используются `with allure.step()` и `attach_screenshot(driver, "Описание")`.
Каждый тест запускается в отдельном Chrome. Браузер работает без окна.

## Файлы для сдачи

- [test_saucedemo.py](test_saucedemo.py) — три теста.
- [conftest.py](conftest.py) — запуск браузера и функция прикрепления скриншота.
- [allure_report.png](allure_report.png) — скриншот страницы настоящего отчёта Allure: 3 теста, 100% успешно.

Скриншоты сайта прикреплены внутри отчёта. Отдельно сдавать их не нужно.

## Установка (PowerShell)

Нужны Python 3.11+, Google Chrome, Node.js/npm и Java 8+ для Allure 2.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
npm.cmd install --prefix .tools allure-commandline@2
```

В этой папке зависимости уже установлены. Selenium Manager автоматически подбирает ChromeDriver при первом запуске; для этого нужен интернет.

## Запуск тестов и отчёта

```powershell
.\.venv\Scripts\python.exe -m pytest -v --alluredir=allure-results --clean-alluredir
.\.tools\node_modules\.bin\allure.cmd generate allure-results -o allure-report --clean
.\.tools\node_modules\.bin\allure.cmd open allure-report
```

Последняя команда откроет отчёт в браузере. Не открывайте HTML отчёта двойным кликом: для его работы нужен локальный сервер, который запускает Allure.
