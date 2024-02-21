import time
from playwright.sync_api import expect
from ...resources.enums.ErrorMessage import ErrorMessage


class LoginForm:
    def __init__(self, page):
        self.page = page
        self.create_account = page.locator('//a[@data-testhook="signup-customer"]')

    def create_new_account(self):
        self.create_account.click()


class CreateAccountForm:
    def __init__(self, page):
        self.page = page
        self.existing_bonus_card = page.locator('//button[@data-testhook="loyalty-optin-form-add-bonusCard"]')
        self.new_bonus_card = page.locator('//button[@data-testhook="loyalty-optin-form-create-bonusCard"]')
        self.bonus_card_with_AH_acc = page.get_by_text('Bonuskaart + Mijn Albert Heijn')
        self.bonus_card_with_no_AH_acc = page.get_by_text('Zonder Mijn Albert Heijn')
        self.next_button = page.get_by_text('Volgende')
        self.email_input = page.locator('//input[@data-testhook="input-field-emailAddress"]')
        self.password_original = page.locator('//input[@data-testhook="input-field-original"]')
        self.error_message_email = page.locator('//div[@data-testhook="error-field-emailAddress"]/p')

    def select_existing_bonus_card(self):
        self.existing_bonus_card.click()

    def add_new_bonus_card(self):
        time.sleep(1)
        self.new_bonus_card.click()

    def select_bonus_card_with_AH_account(self):
        self.bonus_card_with_AH_acc.click()

    def select_bonus_card_without_AH_account(self):
        time.sleep(1)
        self.bonus_card_with_no_AH_acc.click()

    def click_next_button(self):
        self.next_button.click()

    def register_login_credentials(self, email):
        self.email_input.fill(email)

    def validate_error_message_email(self):
        expect(self.error_message_email).to_have_text(ErrorMessage.EMAIL.value)


