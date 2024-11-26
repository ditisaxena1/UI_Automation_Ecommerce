from behave import step

from features.page_objects.cart_page import CartPage


@step("User removes the product - {product_name}")
def step_impl(context, product_name):
    cartpage = CartPage(context.driver)
    cartpage.remove_product(product_name)


@step("Product - {product_name} is removed from the cart")
def step_impl(context, product_name):
    cartpage = CartPage(context.driver)
    if_removed = cartpage.if_product_removed(product_name)
    assert if_removed


@step("Verify that {message} is displayed")
def step_impl(context, message):
    cartpage = CartPage(context.driver)
    assert cartpage.is_cart_empty(message)