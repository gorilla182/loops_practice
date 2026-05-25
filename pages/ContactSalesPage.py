from playwright.sync_api import Page, expect

class ContactSalesPage:

    COUNTRY = 'US'
    DEVELOPERS = '10_99'

    def __init__(self, page: Page):
        self.page = page
        self.contact_sales_button = page.get_by_role('link', name='Contact sales').first

        # Текстовые поля
        self.first_name = page.locator('#form-field-first_name')
        self.last_name = page.locator('#form-field-last_name')
        self.company = page.locator('#form-field-company')
        self.job_title = page.locator('#form-field-job_title')
        self.email = page.locator('#form-field-email')
        self.phone = page.locator('#form-field-phone')

        # Дропдауны
        self.number_of_developers = page.locator('#form-field-number_of_developers')
        self.phone_country_code = page.locator('select[aria-label="Select country for phone number"]')
        self.country = page.locator('#form-field-country')

        # Кнопка отправки
        self.submit_button = page.get_by_role('button', name='Contact')


    def open_form(self):
        self.contact_sales_button.click()

    def fill_form(self, first_name, last_name, company, job_title, email):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company.fill(company)
        self.job_title.fill(job_title)
        self.email.fill(email)
        self.number_of_developers.select_option(self.DEVELOPERS)
        self.country.select_option(self.COUNTRY)
        self.submit_button.click()
        self.page.wait_for_load_state('networkidle')

    def check_filled_form(self, first, last, company, job, email):
        expect(self.first_name).to_have_value(first)
        expect(self.last_name).to_have_value(last)
        expect(self.company).to_have_value(company)
        expect(self.job_title).to_have_value(job)
        expect(self.email).to_have_value(email)


