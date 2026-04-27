class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://seasons-orchards-six.vercel.app/auth"

    def goto(self):
        self.page.goto(self.url)

    def login(self, email, password):
        self.page.fill('input[id="login-email"]', email)
        self.page.fill('input[id="login-password"]', password)

    def click_login(self):
        self.page.click('button[type="submit"]')

    def is_dashboard_visible(self):
        wait_for_url("**/operational", timeout=10000)   
        return self.page.url != self.url