from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = "[data-test='firstName']"
        self.last_name_input = "[data-test='lastName']"
        self.zip_code_input = "[data-test='postalCode']"
        self.continue_button = "[data-test='continue']"
        self.subtotal_label = ".summary_subtotal_label"
        self.tax_label = ".summary_tax_label"
        self.total_label = ".summary_total_label"
        self.finish_button = "[data-test='finish']"
        self.order_complete_message = ".complete-header"

    def fill_checkout_information(self, first_name: str, last_name: str, zip_code: str):
        """Llena los datos del formulario de checkout y continúa."""
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.zip_code_input, zip_code)
        self.page.click(self.continue_button)

    def verify_order_summary(self, expected_subtotal: str, expected_tax: str, expected_total: str):
        """Verifica los totales en la página de resumen de compra."""
        assert self.page.locator(self.subtotal_label).inner_text() == f"Item total: {expected_subtotal}"
        assert self.page.locator(self.tax_label).inner_text() == f"Tax: {expected_tax}"
        assert self.page.locator(self.total_label).inner_text() == f"Total: {expected_total}"

    def finish_purchase(self):
        """Finaliza la compra haciendo clic en el botón de 'Finish'."""
        self.page.click(self.finish_button)

    def verify_order_completion(self):
        """Verifica que el mensaje de orden completada aparece."""
        assert self.page.locator(self.order_complete_message).inner_text() == "Thank you for your order!"
