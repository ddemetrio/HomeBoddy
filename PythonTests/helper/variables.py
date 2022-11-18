from enum import Enum


class VariablesZipCode(Enum):
    """ Переменные для проверок в тесте test_zip_code
    Args:
        code: ZIP-код, который вводится в поле
        message: сообщение-предупреждение
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message

    without_code = (None, 'Enter your ZIP Code')
    incorrect_1 = ('1f', 'Unknown ZIP Code')
    incorrect_2 = ('1111f', 'Unknown ZIP Code')
    incorrect_3 = ('000011', 'Unknown ZIP Code')
    correct = ('00001', None)
    not_in_data_base = ('00011', None)


class VariablesEmailAddresses(Enum):
    """ Переменные для проверок в тесте test_email_address
    Args:
        email: email-адрес, который вводится в поле
        message: сообщение-предупреждение
    """

    def __init__(self, email, message):
        self.email = email
        self.message = message

    without_email = (None, 'Enter your email address')
    wrong_1 = ('test', 'Wrong email')
    wrong_2 = ('test@test', 'Wrong email')
    wrong_3 = ('test.com', 'Wrong email')
    not_valid_1 = ('test @test.com', 'Email is not valid.')
    correct_1 = ('test-1@test.com', None)
    correct_2 = ('TEST1@TEST.COM', None)
