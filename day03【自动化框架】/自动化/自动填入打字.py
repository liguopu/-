from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://dazi.kukuw.com/")

driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/form/ul[6]/li[2]/input").click()

txt = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[1]/div/span").text

txt1 = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[2]/div/span").text

txt2 = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[3]/div/span").text

txt3 = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[4]/div/span").text

txt4 = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[5]/div/span").text

driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[1]/input[2]").send_keys(txt)
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[2]/input[2]").send_keys(txt1)
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[3]/input[2]").send_keys(txt2)
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[4]/input[2]").send_keys(txt3)
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div[5]/input[2]").send_keys(txt4)
