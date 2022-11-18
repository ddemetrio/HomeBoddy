import allure

from PythonTests.helper.page_walk_in_showers import PageWalkInShowers


@allure.title('Проверка отмены заполнения формы проекты')
def test_cancel_project(initial_driver):
    """ Тест проверяет выход из заполнения формы """
    PageWalkInShowers(driver=initial_driver) \
        .go_to_page_walk_in_showers() \
        .input_zip_code() \
        .check_close_form()


