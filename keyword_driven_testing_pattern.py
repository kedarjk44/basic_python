from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class KeywordDrivenTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get("https://example.com")
        sleep(10)

    def enter_text(self, locator, text):
        element = self.driver.find_element(By.ID, locator)
        element.clear()
        element.send_keys(text)

    def click_button(self, locator):
        button = self.driver.find_element(By.ID, locator)
        button.click()

    def close_browser(self):
        self.driver.quit()

# Test case using keywords
test_case = [
    ("open_browser", []),
    ("enter_text", ["username", "john_doe"]),
    ("enter_text", ["password", "secret_password"]),
    ("click_button", ["login_button"]),
    ("close_browser", [])
]

# Execute the test case
kdt = KeywordDrivenTest()
for keyword, args in test_case:
    getattr(kdt, keyword)(*args)
