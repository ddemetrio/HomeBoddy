import allure

from PythonTests.helper.enums import Questions
from PythonTests.helper.page_walk_in_showers import PageWalkInShowers


@allure.title('Позитивные шаги до формы ввода Full name и Email address')
def test_questions(initial_driver):
    """ Тест проходит шаги до формы ввода Full name и Email address """
    PageWalkInShowers(driver=initial_driver) \
        .go_to_page_walk_in_showers() \
        .input_zip_code() \
        .check_question_form(question=Questions.question_1) \
        .click_on_button_next() \
        .check_question_form(question=Questions.question_2) \
        .click_on_button_next() \
        .check_question_form(question=Questions.question_3) \
        .click_on_button_next() \
        .check_question_form(question=Questions.question_4) \
        .click_on_button_next() \
        .check_question_form(question=Questions.question_5) \
        .click_on_button_next() \
        .check_question_form(question=Questions.question_6) \
        .click_on_button_next() \
        .check_question_form(question=Questions.question_7) \
        .click_on_button_next() \
        .check_question_form(question=Questions.question_8) \
        .click_on_button_next()
