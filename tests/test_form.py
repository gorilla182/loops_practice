from pages.HomePage import HomePage
from pages.ContactSalesPage import ContactSalesPage
from pages.CiCdPage import CiCdPage
from pages.SolutionsPage import SolutionsPage
import pytest
from playwright.sync_api import *
from config import *

@pytest.mark.smoke
def test_form(page: Page, open_page):
    home = HomePage(page)
    solutions = SolutionsPage(page)
    contact_sales_page = ContactSalesPage(page)
    cicd_page = CiCdPage(page)

    home.go_to_solutions()
    solutions.select_cicd()
    cicd_page.click_contact_sales()
    contact_sales_page.open_form()
    contact_sales_page.fill_form(FIRSTNAME,LASTNAME, COMPANY, JOB_TITLE, EMAIL)
    contact_sales_page.check_filled_form(FIRSTNAME, LASTNAME, COMPANY, JOB_TITLE, EMAIL)