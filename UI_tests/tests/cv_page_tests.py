from UI_tests.helpers.cv_page import CV_Page


def test_cv_page(cv_page: CV_Page):
    name = 'abcde'
    cv_page.insert_first_name(name)

