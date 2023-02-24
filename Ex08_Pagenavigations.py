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

        driver.back()

        time.sleep(2)

        driver.forward()

        time.sleep(2)

        driver.refresh()

        time.sleep(1)

        driver.close()

if __name__ == '__main__':
    unittest.main()
