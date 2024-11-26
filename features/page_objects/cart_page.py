from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from features.page_objects.base import BasePage


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(driver)

    def remove_product(self, product_name):
        self.base.wait_and_click(By.XPATH, f"//*[text()='{product_name}']/../../td/a[@class='btn btn-sm btn-default']")

    def if_product_removed(self, product_name):
        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, f"(//*[text()='{product_name}'])[1]")))
            return False
        except (TimeoutException, NoSuchElementException):
            return True

    def is_cart_empty(self, text):
        return self.base.is_element_visible(By.XPATH, f"//*[@class='contentpanel' and contains(text(),'{text}')]")