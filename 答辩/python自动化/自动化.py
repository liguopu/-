import unittest

from ddt import ddt, data
from selenium import webdriver
from selenium.webdriver.common.by import By
from HTMLTestRunner import HTMLTestRunner
import os
from excel import aaa


@ddt
class TestHkr(unittest.TestCase):
    @data(*aaa.bbb)
    def testLogin(self, testdata):
        # 准备数据
        name = testdata["姓名"]
        pwd = testdata["密码"]
        expect = testdata["期望结果"]

        # 执行用例
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR/")
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(name)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(pwd)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()

        # 断言
        result = driver.title
        self.assertEqual(expect, result)

        # # 生成测试报告
        # tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="自动化.py")
        # runner = HTMLTestRunner.HTMLTestRunner(
        #     title="HKR测试",
        #     description="hkr登陆测试",
        #     verbosity=1,
        #     stream=open(file="HKR-login.html", mode="w+", encoding="utf-8")
        # )
        # runner.run(tests)
