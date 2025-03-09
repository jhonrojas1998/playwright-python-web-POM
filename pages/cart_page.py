from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item_names = ".inventory_item_name"
        self.cart_item_prices = ".inventory_item_price"
        self.checkout_button = "[data-test='checkout']"

    def verify_cart_items(self, expected_items: dict):
        """Verifica que los productos y sus precios sean correctos en el carrito."""
        items = self.page.locator(self.cart_item_names).all_inner_texts()
        prices = self.page.locator(self.cart_item_prices).all_inner_texts()

        for name, price in expected_items.items():
            assert name in items, f"El producto '{name}' no está en el carrito"
            assert price in prices, f"El precio '{price}' no es el correcto para '{name}'"

    def proceed_to_checkout(self):
        """Hace clic en el botón de checkout."""
        self.page.locator(self.checkout_button).click()
