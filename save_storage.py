from playwright.sync_api import sync_playwright

STORAGE_FILE = "storage_state.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Перейди на страницу авторизации
    page.goto("https://yobamos.veilstaff.com/login?returnUrl=%2Ffeed")

    # Введи логин и пароль
    page.get_by_placeholder("Логин").fill("shkryabin")
    page.get_by_placeholder("Пароль").fill("shkryabinpassword")
    page.get_by_role("button", name="Войти").click()

    # Дождись загрузки страницы после логина
    page.wait_for_selector(".simplebar-content")  # Например, сайдбар

    # Сохрани состояние сессии
    context.storage_state(path=STORAGE_FILE)

    print(f"Файл {STORAGE_FILE} сохранён!")
    browser.close()
