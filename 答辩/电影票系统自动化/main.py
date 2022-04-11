from selenium import webdriver
import unittest
from moviedata import moviedata
from ddt import ddt, data
from selenium.webdriver.common.by import By


@ddt
class TestMovie(unittest.TestCase):
    @data(*moviedata.data0)
    def testAdd(self, data1):
        a1 = data1["影院名称"]
        a2 = data1["联系电话"]
        a3 = data1["影院地址"]
        a4 = data1["乘车路线"]
        a5 = data1["营业时间"]
        a6 = data1["影院所在城市"]
        a7 = data1["影厅介绍"]
        a8 = data1["放映设备"]
        a9 = data1["停车设施"]
        a10 = data1["详细介绍"]
        a11 = data1["期望结果"]

        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/moviemanager/index_loginshow.action")
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="textfield"]').send_keys("admin")
        driver.find_element(By.XPATH, '//*[@id="textfield2"]').send_keys("123456")
        driver.find_element(By.XPATH, '//*[@id="_login_"]').click()
        driver.find_element(By.XPATH,
                            '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td/span/a').click()
        driver.find_element(By.XPATH, '//*[@id="theaterName"]').send_keys(a1)
        driver.find_element(By.XPATH, '//*[@id="tel"]').send_keys(a2)
        driver.find_element(By.XPATH, '//*[@id="address"]').send_keys(a3)
        driver.find_element(By.XPATH, '//*[@id="busLines"]').send_keys(a4)
        driver.find_element(By.XPATH, '//*[@id="businessHours"]').send_keys(a5)
        driver.find_element(By.XPATH, '//*[@id="citychpy"]').send_keys(a6)
        driver.find_element(By.XPATH, '//*[@id="deviceTro"]').send_keys(a7)
        driver.find_element(By.XPATH, '//*[@id="deviceTro"]').send_keys(a8)
        driver.find_element(By.XPATH, '//*[@id="parkTro"]').send_keys(a9)
        driver.find_element(By.XPATH, '/html/body').send_keys(a10)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        result = driver.title
        driver.quit()
        self.assertEqual(a11, result)
