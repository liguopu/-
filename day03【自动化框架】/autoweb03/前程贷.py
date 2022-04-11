from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://8.129.91.152:8765/Index/login.html")

driver.maximize_window()

# 登录模块

# driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[1]/input").send_keys("18337203560")
#
# driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[2]/input").send_keys("liguopu1013...")
#
# driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[5]/button").click()

# 注册模块

driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div[6]/a").click()

driver.find_element(By.XPATH, "//*[@id='phone']").send_keys("18337203563")

driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div[3]/a").click()  # 点击获取验证码按钮

text = driver.find_element(By.CLASS_NAME, "layui-layer-content").text


print(text)

driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div[4]/input").send_keys("liguopu1013...")

driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div[5]/label/input").click()
