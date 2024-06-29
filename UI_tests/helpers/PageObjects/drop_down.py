from UI_tests.helpers.PageObjects.base_object import BaseObject


class DropDown(BaseObject):
    def __init__(self, page, selector: str):
        super().__init__(page, selector)

    def pick_option(self, option_name: str):
        self.element.select_option(option_name)
