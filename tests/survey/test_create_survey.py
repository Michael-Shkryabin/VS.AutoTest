from playwright.sync_api import expect
from datetime import datetime

def open_survey_creation(page):
    page.goto("https://yobamos.veilstaff.com/feed")
    # Открытие сайдбара
    sidebar = page.locator(".simplebar-content")
    sidebar.hover()
    # Открытие вкладки «Опросники» и переход на страницу создания опросника
    page.get_by_role("button", name="Опросники").click()
    page.get_by_role("button", name="Создать Опросник").click()

def test_create_survey(page):
    skill_1 = page.locator("text=Руководство командой")
    skill_2 = page.locator("text=Принятие решений")
    skill_3 = page.locator("text=Делегирование")

    open_survey_creation(page)

    # Проверка названия страницы
    title = page.get_by_role("heading", name = "Создание нового опросника по оценке сотрудников")
    expect(title, "Неверное название страницы").to_have_text("Создание нового опросника по оценке сотрудников")

    # Проверка правильного названия ссылки «Библиотека опросников»
    text_in_header_0 = page.get_by_text("Библиотека опросников")
    expect(text_in_header_0, "Неверный текст в хэдере страницы").to_be_visible()

    # Проверка текста в хэдере страницы
    text_in_header_1 = page.get_by_text("Создание нового опросника по оценке сотрудников").nth(1)
    expect(text_in_header_1, "Неверный текст в хэдере страницы").to_have_text("Создание нового опросника по оценке сотрудников")

    # Переменная для формирования даты для названия опросника
    current_datetime = datetime.now().strftime("%m/%d - %I:%M %p")

    # Проверка поля «Название опросника»
    name_survey = page.get_by_label("Название опросника")
    expect(name_survey, "Поле 'Название опросника' не отображается на странице").to_be_visible()
    name_survey.click()
    name_survey.fill(f"Тестовый опросник {current_datetime}") # Дата нужна для того чтобы не создавать опросники с одинаковым названием

    # Проверка поля «Кратко опишите создаваемый опросник...»
    survey_description = page.get_by_label("Кратко опишите создаваемый опросник...")
    expect(survey_description, "Поле 'Кратко опишите создаваемый опросник...' не отображается на странице").to_be_visible()
    survey_description.click()
    survey_description.fill("Тестовое описание опросника")

    # Проверка поля «Тестируемые навыки»
    input_skills = page.get_by_label("Тестируемые навыки")
    expect(input_skills, "Поле «Тестируемые навыки» не отображается").to_be_visible()
    input_skills.click()
    skill_1.click()
    skill_2.click()
    skill_3.click()

    page.mouse.click(100, 200) # Клик необходим для того чтобы кнопка «Далее» стала активна

    # Проверка кнопки «Далее»
    button_next = page.get_by_role("button", name="Далее")
    expect(button_next, "Кнопка «Далее» не отображается").to_be_visible()
    button_next.click()

    # Проверка кнопки «Основные параметры»
    basic_param_button = page.get_by_role("button", name="Основные параметры")
    expect(basic_param_button, "Кнопка «Основные параметры» не отображается").to_be_visible()
    # basic_param_button.click()
    # expect(button_next, "Кнопка «Основные параметры» не работает").to_be_visible()
    # button_next.click()

    # Проверка кнопки «Добавить новый вопрос»
    add_new_question = page.get_by_role("button", name="Добавить новый вопрос")
    expect(add_new_question, "Кнопка «Добавить новый вопрос» не отображается").to_be_visible()
    add_new_question.click()

    # Проверка полей и кнопок на странице добавления нового вопроса
    input_skil = page.get_by_label("Тестируемый навык")
    expect(input_skil, "Поле «Тестируемый навык» не отображается").to_be_visible()
    input_text_question = page.get_by_label("Введите текст вопроса...")
    expect(input_text_question, "Поле «Введите текст вопроса» не отображается").to_be_visible()
    create_question = page.get_by_role("button", name="Создать вопрос")
    expect(create_question, "Кнопка «Создать вопрос» не отображается").to_be_visible()
    back_button = page.get_by_role("button", name="Назад")
    expect(back_button, "Кнопка «Назад» не отображается").to_be_visible()
    back_button.click()
    add_new_question.click()

    # Функция добавления нового вопроса
    def add_question(skill, text):
        input_skil.click()
        skill.click()
        input_text_question.click()
        input_text_question.fill(text)
        create_question.click()

    add_question(skill_1, "Тестовый вопрос № 1")
    add_new_question.click()
    add_question(skill_2, "Тестовый вопрос № 2")
    add_new_question.click()
    add_question(skill_3, "Тестовый вопрос № 3")

    # Проверка кнопки «Завершить создание»
    button_create_survey = page.get_by_role("button", name="Завершить создание")
    expect(button_create_survey, "Кнопка «Завершить создание» не отображается на странице").to_be_visible()
    # button_create_survey.click()