from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestHkr.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="Hkr测试",
    description="Hkr登录测试",
    verbosity=1,
    stream=open(file="Hkr-login.html", mode="w+", encoding="utf-8")
)
runner.run(tests)
