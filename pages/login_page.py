from playwright.sync_api import Page
from config import USERNAME,PASSWORD, BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        #locators
        self.sign_in_locator_home = page.get_by_role("link", name="Sign in")
        self.user_name_locator = page.get_by_label('Username or email address')
        self.password_locator = page.get_by_label('Password')
        self.sign_in_button = page.locator("xpath=//input[@class='btn btn-primary btn-block js-sign-in-button']")
        self.avatar = page.get_by_test_id("github-avatar")

    def login(self):
        username = USERNAME
        password = PASSWORD
        self.sign_in_locator_home.click()
        self.user_name_locator.fill(username)
        self.password_locator.fill(password)
        self.sign_in_button.click()

