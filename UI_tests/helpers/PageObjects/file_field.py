from UI_tests.helpers.PageObjects.base_object import BaseObject


class FileField(BaseObject):
    def __init__(self, page, selector: str):
        super().__init__(page, selector)

    def input_file(self, file_path: str):
        # self.element.click()
        self.element.set_input_files(file_path)
