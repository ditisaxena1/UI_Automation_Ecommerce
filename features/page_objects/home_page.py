from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from features.page_objects.base import BasePage


class HomePage:

    category_map = {
        'Skincare': 3
    }


    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(driver)

    def search_product(self, product_name, category=None):
        search_box = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='filter_keyword']")))

        search_box.clear()
        search_box.send_keys(product_name)

        if category is not None:
            element = self.driver.find_element(By.XPATH, f"//*[@id='search-category']//*[text()={category}]")
            element.click()

    def click_on_go(self):
        self.driver.find_element(By.XPATH, "//*[@title='Go']").click()

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, "//*[@id='search_button']")

    def select_product(self, product_name):
        self.base.wait_and_click(By.XPATH, f"//*[@class='prdocutname' and text()='{product_name}']")


    def add_to_cart_quantity(self, quantity):
        self.base.remove_and_fill(By.XPATH,f"//*[@id='product_quantity']",quantity)


    def click_add_to_cart(self):
        self.base.wait_and_click(By.XPATH, "//*[@class='cart']")

    def select_product_category(self, category_name, sub_category=None):

        category_box = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,f"//ul[contains(@class,'categorymenu')]//*[contains(text(),'{category_name}')]")))
        actions = ActionChains(self.driver)
        actions.move_to_element(category_box).perform()

        if sub_category is not None:
            element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"(//*[contains(text(),'{category_name}')]/..//*[contains(text(),'{sub_category}')])[1]")))
            actions.move_to_element(element).click().perform()

    def expand_category(self):
        self.base.wait_and_click(By.XPATH, "//*[@id='category_id']")

    def select_category(self, category):
        index = self.category_map[category]
        select = Select(self.driver.find_element(By.XPATH, "//*[@id='category_id']"))
        select.select_by_index(index)


    def if_page_displayed(self, title):
        return self.base.is_page_navigated(title)





