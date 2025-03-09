from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_bike_light = "#item_0_title_link"
        self.product_tshirt = "#item_3_title_link"
        self.add_to_cart_button = "[data-test^='add-to-cart']"
        self.back_to_products = "[data-test='back-to-products']"
        self.cart_badge = ".shopping_cart_badge"
        self.cart_button = ".shopping_cart_link"

    def select_product_and_add_to_cart(self, product_selector: str):
        """Selecciona un producto, entra a su página, lo añade al carrito y vuelve a la lista de productos."""
        self.page.click(product_selector)  # Clic en el producto
        self.page.click(self.add_to_cart_button)  # Clic en "Add to cart"
        self.page.click(self.back_to_products)  # Volver a la lista de productos

    def verify_cart_count(self, expected_count: str):
        """Verifica que el contador del carrito muestra la cantidad esperada."""
        assert self.page.inner_text(self.cart_badge) == expected_count

    def go_to_cart(self):
        """Ir al carrito."""
        self.page.click(self.cart_button)
