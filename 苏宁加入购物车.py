from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.suning.com/")

driver.maximize_window()  # 最大化页面

driver.find_element(By.ID, "searchKeywords").send_keys("草莓")

driver.find_element(By.XPATH, "//*[@id='searchSubmit']").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "新鲜草莓当季草莓红颜奶油冬草莓 3斤(1500克)").click()

driver.switch_to.window(driver.window_handles[-1])

driver.find_element(By.ID, "addCart").click()
