from pages.base_app import BasePage

class LoginPage(BasePage):
    def open(self):
        pass

    def login(self, username, password):
        user = {"id":username, "data": password, "is_login": True}
        return user

    def is_logged_in(self, user):
        return user['is_login']