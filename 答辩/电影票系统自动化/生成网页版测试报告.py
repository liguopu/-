from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="main.py")
runner = HTMLTestRunner.HTMLTestRunner(
    title="movie测试",
    description="movie影院信息增加测试",
    verbosity=1,
    stream=open(file="movie.html", mode="w+", encoding="utf-8")
)
runner.run(tests)
