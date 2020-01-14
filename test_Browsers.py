from selenium import webdriver
from test_Constant_Elements import *
# from webdriver_manager.chrome import ChromeDriverManager

constant = Constants()

class Browser():

    def chrome(self):
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(constant.CHROME)
        driver.maximize_window()
        driver.get(constant.URL)
        return driver

    def firfox(self):
        driver =webdriver.Firefox(executable_path=r'C:\\Drivers\geckodriver.exe')
        driver.maximize_window()
        driver.get(constant.URL)

    def headless(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
        options.add_argument('--window-size=1280x800')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Drivers\chromedriver.exe')
        self.driver.get(constant.URL)