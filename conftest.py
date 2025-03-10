import pytest
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://yobamos.veilstaff.com/login?returnUrl=%2Ffeed"
STORAGE_FILE = "storage_state.json"

@pytest.fixture(scope="session", autouse=True)
def save_auth_session():
    """Фикстура выполняется один раз перед всеми тестами и сохраняет сессию."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)

        page = context.new_page()
        page.goto(LOGIN_URL)

        # Ввод логина и пароля
        page.get_by_placeholder("Логин").fill("shkryabin")
        page.get_by_placeholder("Пароль").fill("shkryabinpassword")
        page.get_by_role("button", name="Войти").click()

        # Дождаться загрузки страницы после входа
        page.wait_for_url("https://yobamos.veilstaff.com/feed")

        # Сохранить сессию
        context.storage_state(path=STORAGE_FILE)

        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(request):
    """Фикстура Playwright:
    - если тест помечен @pytest.mark.ignore_session → создаётся новый контекст (авторизация требуется)
    - иначе используется сохранённая сессия"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])

        if request.node.get_closest_marker("ignore_session"):
            # Создаём новый контекст (авторизация нужна)
            context = browser.new_context(no_viewport=True)
        else:
            # Используем сохранённую сессию (авторизация не требуется)
            context = browser.new_context(no_viewport=True, storage_state=STORAGE_FILE)

        page = context.new_page()
        yield page
        context.close()
        browser.close()
