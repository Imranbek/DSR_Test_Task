from UI_tests.helpers.PageObjects.checkbox import Checkbox
from UI_tests.helpers.PageObjects.instert_fields import InsertField
from UI_tests.helpers.page import Page


class CV_Page(Page):
    FIRSTNAME_FLD = 'input[name="FirstName"]'
    LASTNAME_FLD = 'input[name="LastName"]'

    EMAIL_FLD = 'input[name="Email"]'
    PHONE_FLD = 'input[name="PhoneNumber"]'

    GENDER_MAIL_CHBX = 'input[name="Gender"][value="Male"]'
    GENDER_FEMAIL_CHBX = 'input[name="Gender"][value="Female"]'

    VACANCY_LSTBX = 'select[name="Vacancy"]'
    VACANCY_OPT = {'qa_engineer': 'QA Engineer',
                   'qaa_engineer': 'QAA Engineer',
                   'business_analyst': 'Business Analyst', }
    def __init__(self, browser_context, url :str):
        super().__init__(browser_context, url)

    def open(self):
        super().open()

        self.first_name_field = InsertField(self.page, self.FIRSTNAME_FLD)
        self.last_name_field = InsertField(self.page, self.LASTNAME_FLD)
        self.email_field = InsertField(self.page, self.EMAIL_FLD)
        self.phone_field = InsertField(self.page, self.PHONE_FLD)

        self.gender_mail = Checkbox(self.page, self.LASTNAME_FLD)
        self.gender_femail = Checkbox(self.page, self.LASTNAME_FLD)

        return self.page

    def insert_first_name(self, value):
        self.first_name_field.insert_value(value)


 # EMAIL_FLD = 'input[name="Email"]'
 #    PHONE_FLD = 'input[name="Phone"]'
 #
 #    GENDER_MAIL_CHBX = 'input[name="Gender"][value="Male"]'
 #    GENDER_FEMAIL_CHBX = 'input[name="Gender"][value="Female"]'
 #
 #    VACANCY_BX = 'select[name="Vacancy"]'
 #    VACANCY_OPT = {'qa_engineer': 'QAA Engineer',
 #                   'qa_engineer': 'QAA Engineer',
 #                   'qa_engineer': 'QAA Engineer', }