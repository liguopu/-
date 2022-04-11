class LoginOperation:

    def __init__(self, driver):  # 构造方法，主要保证传进来的driver全局唯一
        self.driver = driver

    def login(self, username, pwd):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

    # 获取成功实际结果
    def getSuccessData(self):
        return self.driver.title

    def getErrordata(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text
