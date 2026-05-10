from pages.login_page import LoginPage

def test_login_success():
    page = LoginPage("driver")
    page.open()
    user = page.login("alex", "1234")
    assert page.is_logged_in(user) == True
