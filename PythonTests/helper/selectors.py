from enum import Enum, unique

from selenium.webdriver.common.by import By


@unique
class LocPage(Enum):
    """ Локаторы на странице Walk-In Showers"""

    def format_value(self, *args):
        """Метод форматирования локаторов"""
        return self.value[0], self.value[1].format(*args)

    xpath_title_question = (By.XPATH, '//h4[contains(text(), "{}")]')
    css_input_zip_code = (By.CSS_SELECTOR, '#zipCode')
    css_try_another_zip_code = (By.CSS_SELECTOR, '#StepBodyId a')
    css_button = (By.CSS_SELECTOR, '#zip_header button')
    xpath_warning_message = (By.XPATH, '//*[@id="zip_header"]//div[contains(@class, "zip--caption")] | '
                                       '//div/div[contains(@class, "mt-1undefined")]')
    css_button_next = (By.CSS_SELECTOR, '#StepBodyId button.Btn.BtnPrimary.Button')
    css_button_answers = (By.CSS_SELECTOR, '#StepBodyId label')
    css_button_close_project = (By.CSS_SELECTOR, '.justify-content-between svg')
    css_button_submit = (By.CSS_SELECTOR, '#StepBodyId button.BtnPrimary')
    css_button_cancel_project = (By.CSS_SELECTOR, '#StepBodyId button.BtnOutline')
    css_input_email = (By.CSS_SELECTOR, '#StepBodyId input')
    xpath_button_yes = (By.XPATH, '//div[contains(text(), "Yes")]')
    xpath_button_no = (By.XPATH, '//div[contains(text(), "No")]')
    css_question_warning_message = (By.CSS_SELECTOR, '#StepBodyId .text-orangeDeep100')
    css = (By.CSS_SELECTOR, '#StepBodyId h4')
