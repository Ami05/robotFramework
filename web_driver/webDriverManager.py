from selenium import webdriver

class webDriverManager():
    _driver = None
    @classmethod
    def get_web_driver(cls,browser):
        if cls._driver is None:
            if(browser.lower())=="chrome":
                cls._driver = webdriver.Chrome("D:\\learn\\python\\Unittest_Framework\\driver\\chromedriver.exe")

        return cls._driver       