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
    def test_all_fields_are_filled(self,
                                   cv_page: CVPage,
                                   test_cv_path: str,
                                   gender: str):
        with allure.step('prepare data for insert fields'):
            first_name = gen_random_string(5, 'l')
            last_name = gen_random_string(5, 'l')
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
            assert json.loads(cv_page.dialog.message) == awaiting_cv_form

    def test_no_fields_are_filled(self,
                                  cv_page: CVPage):
        cv_page.press_submit_button()

        assert ErrorMsg.not_valid_first_name_err in cv_page.page.content(), f'Text "{ErrorMsg.not_valid_first_name_err}" not found on the page'
        assert ErrorMsg.not_valid_last_name_err in cv_page.page.content(), f'Text "{ErrorMsg.not_valid_last_name_err}" not found on the page'
        assert ErrorMsg.not_valid_email_err in cv_page.page.content(), f'Text "{ErrorMsg.not_valid_email_err}" not found on the page'
        assert ErrorMsg.not_valid_phone_number_err in cv_page.page.content(), f'Text "{ErrorMsg.not_valid_phone_number_err}" not found on the page'
        assert ErrorMsg.no_gender_err in cv_page.page.content(), f'Text "{ErrorMsg.no_gender_err}" not found on the page'
        assert ErrorMsg.no_attached_file_err in cv_page.page.content(), f'Text "{ErrorMsg.no_attached_file_err}" not found on the page'
        assert ErrorMsg.no_pers_data_agreement_err in cv_page.page.content(), f'Text "{ErrorMsg.no_pers_data_agreement_err}" not found on the page'
