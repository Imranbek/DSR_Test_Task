import random

from UI_tests.helpers.PageObjects.button import Button
from UI_tests.helpers.PageObjects.checkbox import Checkbox
from UI_tests.helpers.PageObjects.drop_down import DropDown
from UI_tests.helpers.PageObjects.file_field import FileField
from UI_tests.helpers.PageObjects.insert_field import InsertField
from UI_tests.helpers.page import Page


class CVPage(Page):
    FIRSTNAME_FLD = 'input[name="FirstName"]'
    LASTNAME_FLD = 'input[name="LastName"]'
    EMAIL_FLD = 'input[name="Email"]'
    PHONE_FLD = 'input[name="PhoneNumber"]'
    GENDER_MALE_CHBX = 'input[name="Gender"][value="Male"]'
    GENDER_FEMALE_CHBX = 'input[name="Gender"][value="Female"]'
    VACANCY_DROPDOWN = 'select[name="Vacancy"]'
    VACANCY_OPTIONS = ['QA Engineer', 'QAA Engineer', 'Business Analyst']
    CV_INPUT = 'input[name="myfile"]'
    AGREEMENT_CHBX = 'input[name="Agreement"]'
    SUBMIT_BTN = 'input[name="submitbutton"]'

    def __init__(self, browser_context, url: str):
        super().__init__(browser_context, url)

    def open(self):
        super().open()
        self.first_name_fld = InsertField(self.page, self.FIRSTNAME_FLD)
        self.last_name_fld = InsertField(self.page, self.LASTNAME_FLD)
        self.email_fld = InsertField(self.page, self.EMAIL_FLD)
        self.phone_fld = InsertField(self.page, self.PHONE_FLD)

        self.gender_male_box = Checkbox(self.page, self.GENDER_MALE_CHBX)
        self.gender_female_box = Checkbox(self.page, self.GENDER_FEMALE_CHBX)

        self.cv_input_fld = FileField(self.page, self.CV_INPUT)
        self.vacancy_drpdwn = DropDown(self.page, self.VACANCY_DROPDOWN)
        self.agreement_box = Checkbox(self.page, self.AGREEMENT_CHBX)
        self.submit_button = Button(self.page, self.SUBMIT_BTN)

        return self.page

    def insert_first_name(self, value):
        self.first_name_fld.insert_value(value)

    def insert_last_name(self, value):
        self.last_name_fld.insert_value(value)

    def insert_email(self, value):
        self.email_fld.insert_value(value)

    def insert_phone(self, value):
        self.phone_fld.insert_value(value)

    def pick_gender(self, gender: str):
        if gender.lower() == 'random':
            gender = random.choice(['male', 'female'])

        if gender.lower() == 'male':
            self.gender_male_box.click()
        elif gender.lower() == 'female':
            self.gender_female_box.click()

        return gender

    def pick_vacancy(self, vacancy: str):
        if vacancy.lower() == 'random':
            vacancy = random.choice(self.VACANCY_OPTIONS)

        self.vacancy_drpdwn.pick_option(vacancy)

    def pick_agreement(self):
        self.agreement_box.click()

    def input_cv(self, file_path: str):
        self.cv_input_fld.input_file(file_path)

    def press_submit_button(self):
        self.submit_button.click()
