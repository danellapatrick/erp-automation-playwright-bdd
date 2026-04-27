import pytest
from pytest_bdd import scenario, given, when, then
from pages.login_page import LoginPage


@scenario('../features/login.feature', 'User logs in successfully in the Orchard dashboard')
def test_login():
    pass


@given("I open the login page")
def open_login(login_page):
    login_page.goto()


@when("I enter valid username and password")
def enter_credentials(login_page):
    login_page.login("john.doe7@example.com", "StrongPassword123!")


@when("I click on login button")
def click_login(login_page):
    login_page.click_login()
    login_page.page.wait_for_url("**/operational", timeout=10000)


@then("I should be redirected to dashboard")
def verify_dashboard(login_page):
    print("Current URL:", login_page.page.url)
    assert "/operational" in login_page.page.url