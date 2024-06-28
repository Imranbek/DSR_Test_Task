from UI_tests.helpers.PageObjects.base_object import BaseObject


class InsertField(BaseObject):
    def __init__(self, page, selector):
        super().__init__(page, selector)

    def insert_value(self, value: str):
        self.element.click()
        self.element.fill(value)

    def delete_value(self):
        self.element.click()
        self.element.fill('')
