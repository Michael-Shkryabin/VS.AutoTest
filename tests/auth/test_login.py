from playwright.sync_api import expect

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
