import allure
import pytest

from PythonTests.helper.page_walk_in_showers import PageWalkInShowers
from PythonTests.helper.variables import VariablesZipCode, VariablesEmailAddresses


@pytest.mark.parametrize('email', [VariablesEmailAddresses.without_email, VariablesEmailAddresses.wrong_1,
                                   VariablesEmailAddresses.wrong_2, VariablesEmailAddresses.wrong_3,
                                   VariablesEmailAddresses.not_valid_1, VariablesEmailAddresses.correct_1,
                                   VariablesEmailAddresses.correct_2])
@allure.title('Проверка ввода email на странице отсутствия Zip Code [{email.name} - {email.email}]')
def test_email_address(initial_driver, email):
    """ Тест проверяет корректность введенного email"""
    PageWalkInShowers(driver=initial_driver) \
        .go_to_page_walk_in_showers() \
        .input_zip_code(zip_code=VariablesZipCode.not_in_data_base.code) \
        .input_email(email=email.email) \
        .check_warning_message(message_expected=email.message)
