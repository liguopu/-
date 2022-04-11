import random

from testdata import testdata
from ddt import ddt
from ddt import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestCase


@ddt
class TestHkr(TestCase):
    @data(*testdata.data4)
    def testLogin(self, testdatas):
        name = testdatas['loginname']
        pwd = testdatas['password']
        expect = "Student Login"
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR/")
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(name)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(pwd)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        result = driver.title
        if result != expect:
            driver.save_screenshot(name + "_" + pwd + "_" + str(random.randint(10, 1000000)) + ".jpg")
        driver.quit()
        self.assertEqual(expect, result)
