import json

import allure
import pytest

from UI_tests.helpers.cv_page import CVPage
from UI_tests.helpers.errors import CVPageErrorMessages as ErrorMsg
from UI_tests.utils.generators import gen_random_string, gen_random_email, gen_random_number


class TestCVPage:

    @pytest.mark.parametrize('gender', [
        'Male',
        'Female',
    ], ids=['gender male',
            'gender female'
            ])
    def test_all_fields_are_filled_with_diff_gender(self,
                                                    cv_page: CVPage,
                                                    test_cv_path: str,
                                                    gender: str):
        with allure.step('prepare data for insert fields'):
            first_name = gen_random_string(25, 'l')
            last_name = gen_random_string(25, 'l')
            email = gen_random_email()
            phone = str(gen_random_number(length=9))
            vacancy = 'QA Engineer'
        with allure.step('prepare awaiting form'):
            awaiting_cv_form = {
                "FirstName": first_name,
                "LastName": last_name,
                "Email": email,
                "PhoneNumber": phone,
                "Gender": gender,
                "Vacancy": vacancy,
                "CV": {},
                "Agreement": True
            }

        with allure.step('fill the fields'):
            cv_page.insert_first_name(first_name)
            cv_page.insert_last_name(last_name)
            cv_page.insert_email(email)
            cv_page.insert_phone(phone)
            cv_page.pick_gender(gender)
            cv_page.input_cv(test_cv_path)
            cv_page.pick_agreement()

        with allure.step('press submit'):
            cv_page.press_submit_button()

        with allure.step('check the form'):
            dialog_cv_form = json.loads(cv_page.dialog.message)
            assert len(dialog_cv_form) == len(awaiting_cv_form), \
                'Number of elements in CV form in alert is not matching with awaiting CV form'
            for key, value in awaiting_cv_form.items():
                assert dialog_cv_form[key] == value, \
                    f'{key} value is incorrect - ({dialog_cv_form[key]}). {value} awaits.'

    @pytest.mark.parametrize('vacancy', [
        *CVPage.VACANCY_OPTIONS
    ])
    def test_all_fields_are_filled_with_diff_vacancy(self,
                                                     cv_page: CVPage,
                                                     test_cv_path: str,
                                                     vacancy: str):
        with allure.step('prepare data for insert fields'):
            first_name = gen_random_string(5, 'l')
            last_name = gen_random_string(5, 'l')
            email = gen_random_email()
            phone = str(gen_random_number(length=9))
            gender = 'Male'
        with allure.step('prepare awaiting form'):
            awaiting_cv_form = {
                "FirstName": first_name,
                "LastName": last_name,
                "Email": email,
                "PhoneNumber": phone,
                "Gender": gender,
                "Vacancy": vacancy,
                "CV": {},
                "Agreement": True
            }

        with allure.step('fill the fields'):
            cv_page.insert_first_name(first_name)
            cv_page.insert_last_name(last_name)
            cv_page.insert_email(email)
            cv_page.insert_phone(phone)
            cv_page.pick_gender(gender)
            cv_page.input_cv(test_cv_path)
            cv_page.pick_agreement()
            cv_page.pick_vacancy(vacancy)

        with allure.step('press submit'):
            cv_page.press_submit_button()
        with allure.step('check the form'):
            dialog_cv_form = json.loads(cv_page.dialog.message)
            assert len(dialog_cv_form) == len(awaiting_cv_form), \
                'Number of elements in CV form in alert is not matching with awaiting CV form'
            for key, value in awaiting_cv_form.items():
                assert dialog_cv_form[key] == value, \
                    f'{key} value is incorrect ({dialog_cv_form[key]}). {value} awaits.'

    def test_no_fields_are_filled(self,
                                  cv_page: CVPage):
        cv_page.press_submit_button()

        assert ErrorMsg.not_valid_first_name_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.not_valid_first_name_err}" not found on the page'
        assert ErrorMsg.not_valid_last_name_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.not_valid_last_name_err}" not found on the page'
        assert ErrorMsg.not_valid_email_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.not_valid_email_err}" not found on the page'
        assert ErrorMsg.not_valid_phone_number_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.not_valid_phone_number_err}" not found on the page'
        assert ErrorMsg.no_gender_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.no_gender_err}" not found on the page'
        assert ErrorMsg.no_attached_file_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.no_attached_file_err}" not found on the page'
        assert ErrorMsg.no_pers_data_agreement_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.no_pers_data_agreement_err}" not found on the page'

    @pytest.mark.parametrize('phone', [
        str(gen_random_number(length=6)),
        str(gen_random_number(length=13)),
        gen_random_string(9, 'l'),
        gen_random_string(9, 'm'),
        str(gen_random_number(length=8)) + ' ',
        ' ' + str(gen_random_number(length=8)),
        str(gen_random_number(length=4)) + ' ' + str(gen_random_number(length=4)),
        str(gen_random_number(length=4)) + '-' + str(gen_random_number(length=4)),
    ], ids=['length less 7',
            'length bigger 12',
            'string with letters only',
            'string with letters and digits',
            'valid phone plus space',
            'space plus valid phone',
            'valid phone separated with space',
            'phone separated with -'
            ])
    def test_invalid_phone(self,
                           cv_page: CVPage,
                           phone):
        cv_page.insert_phone(phone)
        cv_page.press_submit_button()
        assert ErrorMsg.not_valid_phone_number_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.not_valid_phone_number_err}" not found on the page.' \
            f'Phone {phone} is unexpectedly valid'

    @pytest.mark.parametrize('phone', [
        str(gen_random_number(length=7)),
        str(gen_random_number(length=12)),
    ], ids=['length boundary value 7',
            'length boundary value 12',
            ])
    def test_valid_phone(self,
                         cv_page: CVPage,
                         phone):
        cv_page.insert_phone(phone)
        cv_page.press_submit_button()
        assert ErrorMsg.not_valid_phone_number_err not in cv_page.page.content(), \
            f'Text "{ErrorMsg.not_valid_phone_number_err}" was found on the page' \
            f'Phone {phone} is unexpectedly invalid'

    def test_invalid_length_names(self,
                                  cv_page: CVPage):
        valid_length = 25
        name = gen_random_string(valid_length + 1, 'l')
        cv_page.insert_first_name(name)
        cv_page.insert_last_name(name)
        cv_page.press_submit_button()
        assert ErrorMsg.not_valid_first_name_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.not_valid_first_name_err}" not found on the page.' \
            f'Length {len(name)} for first name is unexpectedly valid'
        assert ErrorMsg.not_valid_last_name_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.not_valid_last_name_err}" not found on the page.' \
            f'Length {len(name)} for last name is unexpectedly valid'

    @pytest.mark.parametrize('phone', [
        str(gen_random_number(length=6)),
        str(gen_random_number(length=13)),
        gen_random_string(9, 'l'),
        gen_random_string(9, 'm'),
        str(gen_random_number(length=8)) + ' ',
        ' ' + str(gen_random_number(length=8)),
        str(gen_random_number(length=4)) + ' ' + str(gen_random_number(length=4)),
        str(gen_random_number(length=4)) + '-' + str(gen_random_number(length=4)),
    ], ids=['length less 7',
            'length bigger 12',
            'string with letters only',
            'string with letters and digits',
            'valid phone plus space',
            'space plus valid phone',
            'valid phone separated with space',
            'phone separated with -'
            ])
    def test_invalid_email(self,
                           cv_page: CVPage,
                           phone):
        cv_page.insert_phone(phone)
        cv_page.press_submit_button()
        assert ErrorMsg.not_valid_phone_number_err in cv_page.page.content(), \
            f'Text "{ErrorMsg.not_valid_phone_number_err}" not found on the page.' \
            f'Phone {phone} is unexpectedly valid'
