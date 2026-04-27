content = """from pytest_bdd import scenario, given, when, then


@scenario('../features/farmers.feature', 'Admin creates a new farmer successfully')
def test_farmers():
    pass


@given("I am logged in as an Supervisor and on the operational dashboard")
def logged_in_supervisor(login_page):
    login_page.goto()
    login_page.login("john.doe7@example.com", "StrongPassword123!")
    login_page.click_login()
    login_page.page.wait_for_url("**/operational", timeout=10000)


@when("I navigate to the farmers page")
def navigate_to_farmers(farmers_page):
    farmers_page.goto()
    farmers_page.page.wait_for_url("**/farm/farmers", timeout=10000)


@when("I click on the 'Add Farmer' button")
def click_add_farmer(farmers_page):
    farmers_page.click_add_farmer()


@then("the Add New Farmer popup should appear")
def verify_add_farmer_popup(farmers_page):
    assert farmers_page.is_add_farmer_popup_visible()
"""

with open('steps/test_farmers_steps.py', 'w') as f:
    f.write(content)
print('Done')