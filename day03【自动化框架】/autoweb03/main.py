from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="HKR测试",
    description="hkr登陆测试",
    verbosity=1,
    stream=open(file="HKR-login.html", mode="w+", encoding="utf-8")
)
runner.run(tests)
