import pytest
from playwright.sync_api import Page
from config import BASE_URL
from pages.login_page import LoginPage


@pytest.fixture
def open_page(page: Page):
    page.goto(BASE_URL)

@pytest.fixture                         # ← добавь эту фикстуру
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)
