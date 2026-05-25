from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.solutions_button = page.get_by_role("button", name="Solutions")

    def go_to_solutions(self):
        self.solutions_button.hover()




