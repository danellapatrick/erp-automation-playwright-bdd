class LoginPage:


    def __init__(self, page):
        self.page = page

        # selectors (keep centralized)
        self.employee_email = "//input[@id='login-email']"
        self.password = "//div[@class='flex flex-col gap-4']//div[2]//div[2]"
        self.login_btn = "//button[normalize-space()='Sign In']"

    def open_login_page(self):
        self.page.goto("https://your-erp-url.com/login")

    def login(self, employee_email, password):
        self.page.fill(self.employee_email,self.employee_email)
        self.page.fill(self.password, password)
        self.page.click(self.login_btn)


    def open_login_page(self):
        self.page.goto("https://seasons-orchards-six.vercel.app/auth")

    def login(self, employee_email, password):
        self.page.fill(self.employee_email, employee_email)
        self.page.fill(self.password, password)
        self.page.click(self.login_btn)

        # wait for successful login (VERY IMPORTANT)
        self.page.wait_for_url("https://seasons-orchards-six.vercel.app/operational")