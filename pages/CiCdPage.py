from playwright.sync_api import Page

class CiCdPage:
    def __init__(self, page: Page):
        self.page = page
        self.cicd_button = page.get_by_role('link', name='CI/CD')

    def click_contact_sales(self):
        self.cicd_button.click()

