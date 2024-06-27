from UI_tests.helpers.PageObjects.base_object import BaseObject


class Checkbox(BaseObject):
    def __init__(self, page, selector:str):
        super().__init__(page, selector)

    def click(self):
        self.element.click()