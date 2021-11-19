from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.jd.com/")

driver.maximize_window()

driver.find_element(By.ID, "key").send_keys("卫衣")

driver.find_element(By.XPATH, "//*[@class='button']").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "李宁（LI-NING）卫衣男女装同款秋冬男子情侣时尚上衣休闲加绒厚连帽卫衣长袖").click()

driver.switch_to.window(driver.window_handles[-1])

driver.find_element(By.PARTIAL_LINK_TEXT, "加入购物车").click()
