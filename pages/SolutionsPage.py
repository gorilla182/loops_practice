from playwright.sync_api import Page
from pages.HomePage import HomePage

class SolutionsPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page = page
        self.cicd = page.get_by_role('button', name='Solutions')
        self.dropdown = page.locator('.NavDropdown-module__dropdown__xm1jd')
        self.all_solutions = self.dropdown.get_by_role("link", name="View all solutions")



    def select_cicd(self):
        self.go_to_solutions()
        self.all_solutions.click()
        self.go_to_solutions()
        self.cicd.click()

