"""
等待的三大方式:
    1.强制等待：
        使用time内的sleep模块，使程序运行到这一行时，强制等待指定的时间。
                优势：简单入门，调试的一把好手
                劣势：只能够单次生效，无法做有效的判断，会浪费大量的时间。

    2.显示等待：
        使用 from selenium.webdriver.wait import WebDriverWait模块，专门等待指定的元素
            WebDriverWait(driver, 10, 0.5).until(lambda el: driver.find_element(By.XPATH, "//*[@class='button']"))
            driver.find_element(By.XPATH, "//*[@class='button']")
            WebDriverWait(webdriver对象，最大等待时长，搜索频率/次)。until(lambda el :指定等待的对象)
            优势：不会浪费很多时间在等页面反应上，
            劣势：必须声明，书写相对来说比较复杂，只对单次生效。

    3.隐式等待：
        import selenium.webdriver
        driver = selenium.webdriver.Chrome()
        driver.implicitly_wait(10)  等待时间为十秒
            针对当前的webdriver对象，隐式等待只需要设置一次，全局内有效，当遇到页面加载时，自动进入隐式等待，
            当加载完毕，或者达到最大等待时长时，隐式等待结束，继续运行下面的程序代码。
                优势：只需设置一次，即使网络卡顿，等待的时间不固定，也不会报错
                劣势：必须等待页面加载完（网页的静态资源也需要等）才能进入下一步操作，而且如果没有找到元素，也会进入隐式等待，达到隐式等待最大时长时才会报错。

    当多个等待一同被调用时，系统的等待时间取决与最长的等待时间。
"""

# 隐式等待：
import selenium.webdriver

driver1 = selenium.webdriver.Chrome()
driver1.implicitly_wait(10)  # 等待时间为十秒

#  显示等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.jd.com/")

driver.maximize_window()

driver.find_element(By.ID, "key").send_keys("卫衣")

WebDriverWait(driver, 10, 0.5).until(lambda el: driver.find_element(By.XPATH, "//*[@class='button']"))
driver.find_element(By.XPATH, "//*[@class='button']").click()

# driver.find_element(By.PARTIAL_LINK_TEXT, "李宁（LI-NING）卫衣男女装同款秋冬男子情侣时尚上衣休闲加绒厚连帽卫衣长袖").click()
#
# driver.switch_to.window(driver.window_handles[-1])
#
# driver.find_element(By.PARTIAL_LINK_TEXT, "加入购物车").click()
