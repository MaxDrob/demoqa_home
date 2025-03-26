from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.exist_icon()

def test_check_username(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.exist_username()

def test_check_password(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.exist_password()