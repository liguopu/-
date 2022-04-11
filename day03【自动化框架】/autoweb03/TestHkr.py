import unittest
import random
from ddt import data
from ddt import ddt
from selenium import webdriver
from InitPage import InitPage
from LoginOperation import LoginOperation
from write import write
from write import write1
import datetime

i = 1
j = 1


@ddt
class TestHkr(unittest.TestCase):
    @data(*InitPage.success_data)
    def testLoginSuccess(self, testdata):
        global i
        i = i + 1
        username = testdata["username"]
        pwd = testdata["pwd"]
        expect = testdata["expect"]

        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()

        login = LoginOperation(driver)

        login.login(username, pwd)

        # 获取实际结果
        result = login.getSuccessData()
        if result != expect:
            driver.save_screenshot(username + "_" + pwd + "_" + str(random.randint(10, 1000000)) + ".jpg")
            write(i, 4, "不通过")
            write(i, 6, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 时间
        else:
            write(i, 4, "通过")
            write(i, 6, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 时间

        driver.quit()

        self.assertEqual(result, expect)

    @data(*InitPage.error_data)
    def testLoginError(self, testdata):
        global j
        j = j + 1
        username = testdata["username"]
        pwd = testdata["pwd"]
        expect = testdata["expect"]

        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()

        login = LoginOperation(driver)

        login.login(username, pwd)

        # 获取实际结果
        result = login.getErrordata()
        if result != expect:
            driver.save_screenshot(username + "_" + pwd + "_" + str(random.randint(10, 1000000)) + ".jpg")
            write1(j, 4, "不通过")
            write1(j, 6, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 时间
        else:
            write1(j, 4, "通过")
            write1(j, 6, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 时间

        driver.quit()

        self.assertEqual(result, expect)


if __name__ == "__main__":
    TestHkr().testLoginSuccess()
