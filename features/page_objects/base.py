from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, by_type, locator, timeout: float = 10):
        """Check if an element is present on the page."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by_type, locator))
            )
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def is_element_visible(self, by_type, locator, timeout=10):
        """Check if an element is visible on the page."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by_type, locator))
            )
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def is_page_navigated(self, page_title: str):
        """Check if page title is present in the page."""
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(page_title))
            return True
        except TimeoutException:
            return False

    def wait_and_click(self, by_type, locator, timeout=10):
        """Wait for an element to be clickable and then click it."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by_type, locator))
        )
        element.click()

    def remove_and_fill(self, by_type, locator, text, timeout=10):
        """Clear an input field and fill it with the provided text."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by_type, locator))
        )
        element.clear()
        element.send_keys(text)

    def javascript_click(self, by_type, locator):
        """Perform a JavaScript click on an element."""
        element = self.driver.find_element(by_type, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """Scroll to the top of the page."""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_till_element_in_view(self, by_type, locator):
        """Scroll until a specific element is in view."""
        element = self.driver.find_element(by_type, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)