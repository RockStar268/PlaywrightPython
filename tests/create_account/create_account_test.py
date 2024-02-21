from ...resources.pageObjects.Navbar import Navbar
from ...resources.components.Forms import LoginForm, CreateAccountForm
import pytest


@pytest.mark.sanity
@pytest.mark.parametrize("email", [
     "test", "test@.nl"])
def test_enter_invalid_email(set_up,email):
    page = set_up
    navbar = Navbar(page)
    forms_login = LoginForm(page)
    forms_cr = CreateAccountForm(page)

    navbar.click_on_my_account()
    forms_login.create_new_account()

    forms_cr.add_new_bonus_card()
    forms_cr.select_bonus_card_without_AH_account()
    forms_cr.click_next_button()

    forms_cr.register_login_credentials(email)
    forms_cr.password_original.click()  # trigger error message by clicking outside of the the email field
    forms_cr.validate_error_message_email()



