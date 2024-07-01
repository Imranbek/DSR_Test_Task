from UI_tests.pages.PageObjects.base_object import BaseObject


class DropDown(BaseObject):
    def __init__(self, page, selector: str):
        super().__init__(page, selector)
        self.option_values = []
        self.get_all_options()

    def pick_option(self, option_name: str):
        self.element.select_option(option_name)

    def get_all_options(self):
        options = self.element.locator('option')

        for i in range(options.count()):
            option_value = options.nth(i).get_attribute('value')
            self.option_values.append(option_value)
