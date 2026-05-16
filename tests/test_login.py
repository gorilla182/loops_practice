from pages.login_page import LoginPage
import pytest
from playwright.sync_api import expect, Page

@pytest.mark.ui
def test_login_success(login_page: LoginPage, open_page):
    login_page.login()
    expect(login_page.avatar).to_be_visible()


