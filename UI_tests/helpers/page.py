class Page:
    def __init__(self, browser_context, url: str):
        self.browser_context = browser_context
        self.url = url
        self.dialog = None
        self.page = None

    def handle_dialog(self, dialog):
        self.dialog = dialog
        dialog.accept()

    def open(self):
        self.page = self.browser_context.new_page()
        self.page.on("dialog", self.handle_dialog)
        self.page.goto(self.url)
        return self.page
