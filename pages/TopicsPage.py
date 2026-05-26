from playwright.sync_api import Page
from config import TOPICS_URL

SEARCH_URL = "https://github.com/search?q={query}&type=repositories"

class TopicsPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(TOPICS_URL)

    def get_topic_items(self):
        heading = self.page.get_by_role("heading", name="All featured topics")
        heading.wait_for(state="visible")
        container = heading.locator("xpath=following-sibling::div[1]")
        topic_names = container.locator("p.f3")
        topic_names.first.wait_for(state="visible")
        return topic_names.all_inner_texts()

    def search(self, query: str):
        self.page.goto(SEARCH_URL.format(query=query))
        self.page.wait_for_load_state("networkidle", timeout=20_000)

    def get_search_result_items(self):
        return self.page.locator("[data-testid='results-list'] > div")


