import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_purchase_flow(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # 1. Ir al sitio y hacer login
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # 2. Seleccionar y añadir "Sauce Labs Bike Light"
    inventory_page.select_product_and_add_to_cart(inventory_page.product_bike_light)

    # 3. Seleccionar y añadir "Test.allTheThings() T-Shirt (Red)"
    inventory_page.select_product_and_add_to_cart(inventory_page.product_tshirt)

    # 4. Verificar que el contador del carrito muestra "2"
    inventory_page.verify_cart_count("2")

    # 5. Ir al carrito
    inventory_page.go_to_cart()

    # 6. Verificar productos en el carrito
    expected_items = {
        "Sauce Labs Bike Light": "$9.99",
        "Test.allTheThings() T-Shirt (Red)": "$15.99"
    }
    cart_page.verify_cart_items(expected_items)

    # 7. Proceder al checkout
    cart_page.proceed_to_checkout()

    # 8. Diligenciar datos de checkout
    checkout_page.fill_checkout_information("Jhon Hader", "Rojas", "12345")

    # 9. Verificar totales y finalizar compra
    checkout_page.verify_order_summary("$25.98", "$2.08", "$28.06")
    checkout_page.finish_purchase()

    # 10. Verificar mensaje final
    checkout_page.verify_order_completion()
