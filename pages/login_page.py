from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def navigate(self):
        """Navega a la página de login."""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        """Realiza el inicio de sesión con las credenciales proporcionadas."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_successful(self):
        """Verifica que el login fue exitoso revisando si el inventario está visible."""
        expect(self.page.locator(".inventory_list")).to_be_visible()
