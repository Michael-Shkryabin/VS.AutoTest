import pytest
from playwright.sync_api import expect

@pytest.mark.ignore_session # Этот тест не будет использовать сохранённую сессию
def test_login(page):  # test_ в начале обязательно!
    page.goto("https://yobamos.veilstaff.com/login?returnUrl=%2Ffeed")

    # Проверка поля «Логин»
    login_input = page.get_by_placeholder("Логин")
    expect(login_input, "Плейсхолдер 'Логин' не отображается в поле").to_be_visible()
    login_input.click()
    login_input.fill("shkryabin")

    # Проверка поля «Пароль»
    password_input = page.get_by_placeholder("Пароль")
    expect(password_input, "Плейсхолдер 'Пароль' не отображается в поле").to_be_visible()
    password_input.click()
    password_input.fill("shkryabinpassword")

    # Проверка кнопки «Войти»
    login_button = page.get_by_role("button", name="Войти")
    expect(login_button, "Кнопка 'Войти' не отобраажется на странице").to_be_visible()
    login_button.click()

    # Раскрытие сайдбара
    sidebar = page.locator(".simplebar-content")
    sidebar.hover()

    # Проверка кнопки «Выйти»
    logout_button = page.get_by_role("button", name="Выйти")
    logout_button.wait_for(state="visible")
    expect(logout_button, "Кнопка 'Выйти' не отобраажется на странице").to_be_visible()
    logout_button.click()
@pytest.mark.ignore_session
def test_wrong_login(page):
    page.goto("https://yobamos.veilstaff.com/login?returnUrl=%2Ffeed")

    login_input = page.get_by_placeholder("Логин")
    login_input.click()
    login_input.fill("wronglogin")

    password_input = page.get_by_placeholder("Пароль")
    password_input.click()
    password_input.fill("wrongpassword")

    login_button = page.get_by_role("button", name="Войти")
    login_button.click()

    expect(login_input, "Поле 'Логин' не подсвечивается розовым").to_have_attribute("aria-invalid", "true")
    expect(password_input, "Поле 'Пароль' не подсвечивается розовым").to_have_attribute("aria-invalid", "true")
    expect(page.get_by_text("Логин или пароль введены неверно")).to_be_visible()