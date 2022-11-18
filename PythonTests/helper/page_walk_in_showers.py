from __future__ import annotations

import allure

from PythonTests.helper.enums import title_cancel_project, Questions, title_no_contractors
from PythonTests.helper.selectors import LocPage
from PythonTests.ui_basic_methods import BasicMethods


class PageWalkInShowers(BasicMethods):

    def go_to_page_walk_in_showers(self) -> PageWalkInShowers:
        with allure.step('Переход на страницу Walk-In Showers'):
            self.get_url(url='https://hb-beta.stage.sirenltd.dev/walk-in-showers')
        return self

    def click_on_button_close_project(self) -> PageWalkInShowers:
        with allure.step('Нажатие на кнопку закрытия формы'):
            self.element_presence(locator=LocPage.css_button_close_project.value).click()
        return self

    def check_close_form(self) -> PageWalkInShowers:
        with allure.step('Проверка формы отмены проекта'):
            self.element_presence(locator=LocPage.css_button_answers.value)
            self.click_on_button_close_project()
            self.check_title_of_question(question=title_cancel_project)
            with allure.step('Нажатие на кнопку Return to project. Проверка возврата на форму заполнения проекта'):
                self.element_presence(locator=LocPage.css_button_submit.value).click()
                self.element_presence(locator=LocPage.css_button_answers.value,
                                      message='Не произошел переход на предыдущую форму').click()
            self.click_on_button_close_project()
            with allure.step('Нажатие на кнопку Cancel project'):
                self.element_presence(locator=LocPage.css_button_cancel_project.value).click()
                self.element_presence(locator=LocPage.css_input_zip_code.value,
                                      message='Не произошел возврат на главную страницу')
        return self

    def check_title_of_question(self, question: str) -> PageWalkInShowers:
        with allure.step('Проверка вопроса на форме'):
            self.element_presence(locator=LocPage.xpath_title_question.format_value(question),
                                  message=f'Не найден заголовок {question}')
        return self

    def input_zip_code(self, zip_code: str = '00001') -> PageWalkInShowers:
        with allure.step('Ввод ZIP Code'):
            if zip_code:
                input_area = self.element_presence(locator=LocPage.css_input_zip_code.value)
                input_area.send_keys(zip_code)
            self.element_presence(locator=LocPage.css_button.value).click()
        return self

    def check_warning_message(self, message_expected: str) -> PageWalkInShowers:
        with allure.step('Проверка сообщения-предупреждения о некорректном вводе'):
            if message_expected:
                message_fact = self.element_presence(locator=LocPage.xpath_warning_message.value).text
                assert message_fact == message_expected, f'Некорректное сообщение-предупреждение. ' \
                                                         f'Ожидается: {message_expected}. ' \
                                                         f'Фактически: {message_fact}'
        return self

    def input_email(self, email: str) -> PageWalkInShowers:
        with allure.step('Ввод Email address'):
            if email:
                input_area = self.element_presence(locator=LocPage.css_input_email.value)
                input_area.send_keys(email)
        self.element_presence(locator=LocPage.css_button_submit.value).click()
        return self

    def check_page_no_contractors(self) -> PageWalkInShowers:
        with allure.step('Проверка страницы с отсутствием подрядчиков'):
            self.check_title_of_question(question=title_no_contractors)
            self.element_presence(locator=LocPage.css_input_email.value)
            self.element_presence(locator=LocPage.css_button_submit.value)
        return self

    def click_on_button_try_another_zip_code(self) -> PageWalkInShowers:
        with allure.step('Нажатие на кнопку Try another ZIP Code'):
            self.element_presence(locator=LocPage.css_try_another_zip_code.value).click()
            self.element_presence(locator=LocPage.css_input_zip_code.value,
                                  message='Не произошел возврат на главную страницу')
            return self

    def check_button_next(self, disabled: bool = True) -> PageWalkInShowers:
        with allure.step('Проверка кнопки Next'):
            button_next = self.element_presence(locator=LocPage.css_button_next.value)
            disabled_fact = bool(button_next.get_attribute('disabled'))
            if disabled:
                assert disabled_fact, 'Кнопка активна. Ожидается, что при первом открытии страницы кнопка неактивна'
            else:
                assert disabled_fact is False, 'Кнопка неактивна. Ожидается, что при выборе вариантов ' \
                                               'ответа кнопка становится активной'
        return self

    def click_on_button_next(self) -> PageWalkInShowers:
        with allure.step('Нажатие на кнопку Next'):
            self.element_presence(locator=LocPage.css_button_next.value).click()
        return self

    def check_question_warning_message(self, question: str) -> PageWalkInShowers:
        with allure.step('Проверка сообщения-предупреждения в вопросах'):
            warning_message = self.element_presence(locator=LocPage.css_question_warning_message.value)
            assert warning_message.text == question, f'Не совпадает сообщение-предупреждение. ' \
                                                     f'Ожидается: {question}. ' \
                                                     f'Фактически: {warning_message.text}'
        return self

    def check_question_form(self, question: Questions) -> PageWalkInShowers:
        self.check_title_of_question(question.value['title'])
        with allure.step('Проверка неактивности кнопки Next'):
            self.check_button_next()
        with allure.step('Проверка кнопок вариантов ответа'):
            buttons = self.list_of_elements_presence(locator=LocPage.css_button_answers.value)
            for index, button in enumerate(buttons):
                with allure.step('Проверка названия кнопки'):
                    choice = 'choice_' + str(index + 1)
                    assert button.text == question.value[choice], f'Не совпадают варианты ответов. ' \
                                                                  f'Ожидается: {question.value[choice]}. ' \
                                                                  f'Фактически: {button.text}'
                with allure.step(f'Нажатие на вариант ответа {button.text}'):
                    buttons[index].click()
        if question in (Questions.question_4, Questions.question_6):
            self.check_question_warning_message(question=question.value['message'])
            self.element_presence(locator=LocPage.xpath_button_yes.value).click()
        if question in (Questions.question_5, Questions.question_7):
            self.element_presence(locator=LocPage.xpath_button_yes.value).click()
            self.check_question_warning_message(question=question.value['message'])
            self.element_presence(locator=LocPage.xpath_button_no.value).click()
        with allure.step('Проверка активности кнопки Next'):
            self.check_button_next(disabled=False)
        return self
