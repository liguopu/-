from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt
from unittest import TestCase
from ddt import data
from hkrdata import HkrData


@ddt
class TestHkr(TestCase):
    @data(*HkrData.data1)
    def testLongin(self, data2):
        name = data2["姓名"]
        pwd = data2["密码"]
        expect = "Student Login"

        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()

        driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(name)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(pwd)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        result = driver.title

        self.assertEqual(expect, result)
        driver.quit()
