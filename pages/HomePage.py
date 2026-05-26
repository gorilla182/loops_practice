from playwright.sync_api import Page
from config import TOPICS_URL

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.solutions_button = page.get_by_role("button", name="Solutions")

    def go_to_solutions(self):
        self.solutions_button.hover()

    def go_to_topics(self):
        self.page.goto(TOPICS_URL)
        self.page.wait_for_load_state('networkidle')






