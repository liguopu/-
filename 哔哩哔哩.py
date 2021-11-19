from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  #

driver.get("https://www.bilibili.com/")

driver.maximize_window()
driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.PARTIAL_LINK_TEXT, "登录").click()
time.sleep(10)
driver.switch_to.window(driver.window_handles[-1])

driver.find_element(By.CLASS_NAME, "nav-search-keyword").send_keys("每天一遍，大脑再见")

driver.find_element(By.CLASS_NAME, "nav-search-btn").click()

driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "“每天一遍 大脑再见”").click()

driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.find_element(By.CLASS_NAME, "like").click()
