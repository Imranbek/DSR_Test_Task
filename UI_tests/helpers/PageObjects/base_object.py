class BaseObject:
    def __init__(self, page, selector):
        self.element = page.locator(selector)
        if self.element.count() == 0:
            raise ValueError(f"Element with selector {selector} not found")