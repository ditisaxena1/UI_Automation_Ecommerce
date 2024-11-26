from behave import step

from features.page_objects.home_page import HomePage


@step("User is on Automation Test Store Website")
def step_impl(context):
    assert context.driver.current_url == context.base_url


@step("User search for product - {product_name} and optional category - {category_name}")
def step_impl(context, product_name, category_name):
    homepage = HomePage(context.driver)
    if category_name == "None":
        homepage.search_product(product_name)
    else:
        homepage.search_product(product_name, category_name)


@step("User clicks on Go button")
def step_impl(context):
    homepage = HomePage(context.driver)
    homepage.click_on_go()


@step("User selects the product '{product_name}'")
def step_impl(context, product_name):
    homepage = HomePage(context.driver)
    homepage.select_product(product_name)


@step('Verify that user is navigated to {page_name} page')
def step_impl(context, page_name):
    homepage = HomePage(context.driver)
    if_page = homepage.if_page_displayed(page_name)
    assert if_page, "User is on wrong page"


@step("User click on add to cart button")
def step_impl(context):
    homepage = HomePage(context.driver)
    homepage.click_add_to_cart()


@step('User add {quantity} product')
def step_impl(context, quantity):
    homepage = HomePage(context.driver)
    homepage.add_to_cart_quantity(quantity)


@step('User selects the category - {category_name} and optional sub category - {sub_category}')
def step_impl(context, category_name, sub_category):
    homepage = HomePage(context.driver)
    if sub_category == "None":
        homepage.select_product_category(category_name)
    else:
        homepage.select_product_category(category_name, sub_category)


@step('User clicks on Category drop down')
def step_impl(context):
    homepage = HomePage(context.driver)
    homepage.expand_category()


@step('User selects the category {category_name}')
def step_impl(context,category_name):
    homepage = HomePage(context.driver)
    homepage.select_category(category_name)


@step('User clicks on Search')
def step_impl(context):
    homepage = HomePage(context.driver)
    homepage.click_on_search_button()
