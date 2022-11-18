import allure
import pytest

from PythonTests.helper.page_walk_in_showers import PageWalkInShowers
from PythonTests.helper.variables import VariablesZipCode


@pytest.mark.parametrize('zip_code', [VariablesZipCode.without_code, VariablesZipCode.incorrect_1,
                                      VariablesZipCode.incorrect_2, VariablesZipCode.incorrect_3,
                                      VariablesZipCode.correct, VariablesZipCode.not_in_data_base])
@allure.title('Ввод ZIP Code. [{zip_code.name} - {zip_code.code}]')
def test_zip_code(initial_driver, zip_code):
    """ Тест проверяет корректность введенного ZIP Code"""
    PageWalkInShowers(driver=initial_driver) \
        .go_to_page_walk_in_showers() \
        .input_zip_code(zip_code=zip_code.code) \
        .check_warning_message(message_expected=zip_code.message)
    if zip_code == VariablesZipCode.not_in_data_base:
        PageWalkInShowers(driver=initial_driver) \
            .check_page_no_contractors()\
            .click_on_button_try_another_zip_code()
