import unittest
from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):
    def test01(self):
        filePath = "C:\\Users\\HP\\PycharmProjects\\SeleniumProject\\drivers\\chromedriver.exe"

        url = "https://parabank.parasoft.com/parabank/index.htm"

        driver = webdriver.Chrome(filePath)

        time.sleep(1)

        driver.get(url)

        time.sleep(1)

        # Capture Current URL
        pageURL = driver.current_url
        print("Parabank Page URL is --> " + pageURL)

        # Capture Page Title
        pageTitle = driver.title
        print("Parabank Page Title is --> " + pageTitle)

        # Capture Page Source
        # pageSourceCode = driver.page_source
        # print("Parabank Page Source is --> " + pageSourceCode)

        time.sleep(1)

        driver.quit()

if __name__ == '__main__':
    unittest.main()
