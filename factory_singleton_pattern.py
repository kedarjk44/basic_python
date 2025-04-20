from selenium import webdriver

class WebDriverFactory:
    def create_web_driver(self, browser_name):
        if browser_name == "chrome":
            return webdriver.Chrome()
        elif browser_name == "edge":
            return webdriver.Edge()
        else:
            raise ValueError("Invalid browser name")

class WebDriverProvider:
    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.web_driver_factory = WebDriverFactory()

    def get_web_driver(self):
        return self.web_driver_factory.create_web_driver(self.browser_name)

from selenium import webdriver

class WebDriverSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, browser_name):
        if not hasattr(self, "_driver"):
            if browser_name == "chrome":
                self._driver = webdriver.Chrome()
            elif browser_name == "edge":
                self._driver = webdriver.Edge()
            else:
                raise ValueError("Invalid browser name")

    def get_driver(self):
        return self._driver

# Factory Pattern
web_driver_provider = WebDriverProvider("chrome")
driver = web_driver_provider.get_web_driver()

# Singleton Pattern
driver_singleton = WebDriverSingleton("edge")
driver2 = driver_singleton.get_driver()